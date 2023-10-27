from typing import Text, Optional
from typing import Union, Iterable


class DataSave:
    def image_save(image_url: Text,
                   image_path: Union[Text, bytes],
                   astrict: Optional = 100,
                   **kwargs):
        pass

    def images_save(image_iteration: Iterable[Iterable[Text, Text]],
                    astrict: Optional = 100,
                    **kwargs): pass


data_save = DataSave
