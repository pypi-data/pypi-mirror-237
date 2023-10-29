
import os
import logging

from .individualize import Individualize
from .grouping import Grouping
from .visualize import Visualize

class FanesisPipeline:
    def __call__(
        self,
        imgs_path: str,
        base_path: str,
        verbose: bool = True
    ):
        if verbose:
            logging.basicConfig(level=logging.INFO)
        else:
            logging.basicConfig(level=logging.WARNING)
            
        self.imgs_path = imgs_path
        self.base_path = base_path
        self.output_path = os.path.join(base_path, "output/")

        i = Individualize(imgs_path, base_path)
        g = Grouping(self.output_path)
        v = Visualize(self.output_path)
        
        logging.info("Start individualizing..")
        i.run()
        logging.info("Start grouping..")
        df = g.run()
        logging.info("Start visualizing..")
        v.visualize(df)
        
        