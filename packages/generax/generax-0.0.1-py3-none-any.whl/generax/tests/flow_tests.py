import jax
import jax.numpy as jnp
from jax import random
from functools import partial
from typing import Optional, Mapping, Tuple, Sequence, Union, Any, Callable
import einops
import equinox as eqx
from abc import ABC, abstractmethod
from jaxtyping import Array, PRNGKeyArray
import generax.nn.util as util
from generax.flows.base import BijectiveTransform

def run_test(layer_init):
  key = random.PRNGKey(0)
  x = random.normal(key, shape=(10, 2))
  layer = layer_init(input_shape=x.shape[1:], key=key)

  z, log_det = layer(x[0])
  x_inv, log_det_inv = layer.inverse(z)

  z, log_det = eqx.filter_vmap(layer)(x)
  eqx.filter_vmap(layer.inverse)(z)

def inverse_test(layer_init):
  key = random.PRNGKey(0)
  x = random.normal(key, shape=(10, 2))
  layer = layer_init(input_shape=x.shape[1:], key=key)

  z, log_det = eqx.filter_vmap(layer)(x)
  x_reconstr, log_det2 = eqx.filter_vmap(layer.inverse)(z)
  assert jnp.allclose(x, x_reconstr)
  assert jnp.allclose(log_det, -log_det2)

def log_det_test(layer_init):
  key = random.PRNGKey(0)
  x = random.normal(key, shape=(10, 2))
  layer = layer_init(input_shape=x.shape[1:], key=key)

  def jacobian(x):
    return jax.jacobian(lambda x: layer(x)[0])(x)

  _, log_det = eqx.filter_vmap(layer)(x)
  G = eqx.filter_vmap(jacobian)(x)
  assert jnp.allclose(log_det, jnp.linalg.slogdet(G)[1])

def image_run_test(layer_init):
  pass

def image_inverse_test(layer_init):
  pass

def image_log_det_test(layer_init):
  pass


if __name__ == '__main__':
  from debug import *
  # Turn on x64
  from jax.config import config
  config.update("jax_enable_x64", True)

  # Get all of the layers from the flows library
  import generax.flows.affine as flows
  import generax.flows.spline as flows
  import generax.flows.reshape as flows


  # Get a list of of the layers defined in the module
  layer_inits = []
  for name in dir(flows):
    t = getattr(flows, name)
    if isinstance(t, eqx._module._ModuleMeta) and (name != 'BijectiveTransform'):
      layer_inits.append(t)

  # Run the tests
  for flow_init in layer_inits:
    run_test(flow_init)
    inverse_test(flow_init)
    log_det_test(flow_init)
    print(f'Passed tests for {flow_init}')

  import pdb; pdb.set_trace()