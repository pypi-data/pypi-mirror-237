from .layer import GridLayerException
from pydeck.bindings.layer import Layer


class MaskLayer(Layer):
    def __init__(self, mask_url="", id=None, **kwargs):
        """Configures a deck.gl masking layer for creating transparent cutouts. Useful for creating clean shorelines for ocean data.

        Args:
            mask_url : str, default ""
                URL of the masking tileset. Must be a valid URL to a vector tile tileset following the same conventions as the deck.gl MVTLayer.
                All of the tileset's features will be used to mask the data layer.


        Raises:
            GridLayerException
                missing or invalid arguments

        """

        super().__init__(type="MaskLayer", mask_url=mask_url, id=id, **kwargs)
