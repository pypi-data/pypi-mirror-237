import torch
from torch import nn
from linearinit.base import FullyConnectedLayers
import numpy as np
from . import utils


class VAE(nn.Module):
    def __init__(
        self,
        input_size: int,
        layers: int,
        latent_dim: int,
        activation=nn.GELU(),
    ):
        super().__init__()

        self.latent_dim = latent_dim
        self.input_size = input_size
        latent_power = np.floor(np.log2(latent_dim))
        input_power = np.ceil(np.log2(input_size))

        self.layer_sizes = np.logspace(
            input_power + 2, latent_power, layers, base=2.0
        ).astype(int)
        self.layer_sizes[0] = input_size
        self.layer_sizes[-1] = latent_dim

        print("layers sizes: ", self.layer_sizes)

        self.encoder = FullyConnectedLayers(self.layer_sizes)
        self.mu = nn.Linear(self.latent_dim, self.latent_dim)
        self.logvar = nn.Linear(self.latent_dim, self.latent_dim)
        self.decoder = FullyConnectedLayers(self.layer_sizes[::-1])

    def forward(self, x):
        """Perform a single forward pass through the network.

        :param x: The input tensor.
        :return: A tensor of predictions.
        """
        x = self.encoder(x)
        mu = self.mu(x)
        logvar = self.logvar(x)
        z = utils.reparameterization(mu, logvar)
        return self.decoder(z), mu, logvar, z


class SSVAER(nn.Module):
    """Semi-supervised variational autoencoder with regression (SSVAER) model."""

    def __init__(
        self,
        input_size: int,
        shared_layers: int,
        resample_layers: int,
        resample_size: int,
        regressor_layers: int,
        latent_size: int,
        activation=nn.GELU(),
    ):
        super().__init__()

        self.latent_dim = latent_size
        self.input_size = input_size
        self.resample_size = resample_size

        self.shared_layer_sizes = utils.generate_layer_sizes(
            input_size, resample_size, shared_layers, how="logspace"
        )
        self.resample_layer_sizes = utils.generate_layer_sizes(
            resample_size, latent_size, resample_layers, how="linspace"
        )
        self.regressor_layer_sizes = utils.generate_layer_sizes(
            resample_size, 1, regressor_layers, how="linspace"
        )
        self.latent_gen_layer_sizes = utils.generate_layer_sizes(
            2, latent_size, 2
        )

        print("shared layers sizes: ", self.shared_layer_sizes)
        print("resample layers sizes: ", self.resample_layer_sizes)
        print("regressor layers sizes: ", self.regressor_layer_sizes)
        print("latent generator layers sizes: ", self.latent_gen_layer_sizes)

        self.encoder = FullyConnectedLayers(self.shared_layer_sizes)

        self.z_mu = FullyConnectedLayers(self.resample_layer_sizes)
        self.z_logvar = FullyConnectedLayers(self.resample_layer_sizes)

        self.y_mu = FullyConnectedLayers(self.regressor_layer_sizes)
        self.y_logvar = FullyConnectedLayers(self.regressor_layer_sizes)

        self.trend_regressor = FullyConnectedLayers(self.regressor_layer_sizes)

        self.latent_generator = FullyConnectedLayers(
            self.latent_gen_layer_sizes
        )

        self.decoder = FullyConnectedLayers(
            self.resample_layer_sizes[::-1] + self.shared_layer_sizes[::-1]
        )

    def forward(self, x):
        """Performs a single forward pass through the network.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
                - x_hat (torch.Tensor): A tensor of predictions.
                - z_mu (torch.Tensor): The mean of the latent variable z.
                - z_logvar (torch.Tensor): The log variance of the latent variable z.
                - z_resample (torch.Tensor): A resampled tensor of the latent variable z.
                - y_mu (torch.Tensor): The mean of the latent variable y.
                - y_logvar (torch.Tensor): The log variance of the latent variable y.
                - y_resample (torch.Tensor): A resampled tensor of the latent variable y.
                - dy_mu (torch.Tensor): The mean of the trend regressor.
                - z_gen (torch.Tensor): The generated latent variable z.
                - z_gen_resample (torch.Tensor): A resampled tensor of the generated latent variable z.
                - x_gen_hat (torch.Tensor): A tensor of generated predictions.
        """
        x = self.encoder(x)
        z_mu = self.z_mu(x)
        z_logvar = self.z_logvar(x)
        z_resample = utils.reparameterization(z_mu, z_logvar)
        y_mu = self.y_mu(x)
        y_logvar = self.y_logvar(x)
        y_resample = utils.reparameterization(y_mu, y_logvar)
        dy_mu = self.trend_regressor(x)
        x_hat = self.decoder(z_resample)
        latent_gen_input = torch.cat((y_resample, dy_mu), dim=1)
        z_gen = self.latent_generator(latent_gen_input)
        z_gen_resample = utils.reparameterization(
            z_gen, torch.ones_like(z_gen, device=z_gen.device)
        )
        z_gen_resample = z_gen_resample.detach()
        x_gen_hat = self.decoder(z_gen_resample)

        return (
            x_hat,
            z_mu,
            z_logvar,
            z_resample,
            y_mu,
            y_logvar,
            y_resample,
            dy_mu,
            z_gen,
            z_gen_resample,
            x_gen_hat,
        )
