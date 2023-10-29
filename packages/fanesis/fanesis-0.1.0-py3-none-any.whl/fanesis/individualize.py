import os
import glob
import torch
import logging

from tqdm import tqdm
from typing import Union
from deepface import DeepFace
from .utils import save, cos_sim

class Individualize:
    def __init__(
        self, 
        imgs_path: str,
        base_path: str, 
        file_type: str = "jpg", 
        embed_model: str = "Facenet",
        verbose: bool = True
    ):

        if verbose:
            logging.basicConfig(level=logging.INFO)
        else:
            logging.basicConfig(level=logging.WARNING)
        
        self.imgs = glob.glob(imgs_path + f"*.{file_type}")
        logging.info(f"Found {len(self.imgs)} images")
        self.unique_person_counter = 0
        self.embed_model = embed_model
        logging.info(f"Using {self.embed_model} as embed model")
        logging.info(f"Creating output and embed directory at {base_path}")
        self.path, self.embed_path = self.create_dirs(base_path)
        
    
    def run(self) -> None:
        for i, img in tqdm(enumerate(self.imgs)):
            crop_all = DeepFace.extract_faces(img)
            if i == 0: # first image
                for j, crop in enumerate(crop_all):
                    crop = crop["face"]
                    img_dir = os.path.join(self.path, f"person_{j}")
                    if not os.path.isdir(img_dir):
                        os.mkdir(img_dir)
    
                    save(f"{img_dir}/{i}_person {self.unique_person_counter}.jpg",
                        crop)
         
                    embed = torch.tensor(
                                    DeepFace.represent(
                                            crop, 
                                            model_name=self.embed_model, 
                                            detector_backend="skip"
                                        )[0]["embedding"]
                                    )
                    torch.save(embed, f"{self.embed_path}/{i}_person {self.unique_person_counter}.pt")
                    self.unique_person_counter += 1
            else:
                for j, crop in enumerate(crop_all):
                    crop = crop["face"]
                    is_exist, embed_found = self.compare_embed(
                                        torch.tensor(
                                            DeepFace.represent(
                                                crop, 
                                                model_name=self.embed_model, 
                                                detector_backend="skip"
                                            )[0]["embedding"]
                                        ), threshold=0.7
                                    )
                    
                    if is_exist != False:
                        person = embed_found.split("\\")[-1].split("_")[0]
                        img_dir = os.path.join(self.path, f"person_{person}")
                        save(f"{img_dir}/{i}_person {person}.jpg",crop)
                        embed = torch.tensor(
                                            DeepFace.represent(
                                                crop, 
                                                model_name=self.embed_model, 
                                                detector_backend="skip"
                                            )[0]["embedding"]
                                        )
                        torch.save(embed, f"{self.embed_path}/{i}_person {person}.pt")
                    else:
                        img_dir = os.path.join(self.path, f"person_{self.unique_person_counter}")
                        if not os.path.isdir(img_dir):
                            os.mkdir(img_dir)
                            
                        save(f"{img_dir}/{i}_person {self.unique_person_counter}.jpg", crop)
                        embed = torch.tensor(
                                            DeepFace.represent(
                                                crop, 
                                                model_name=self.embed_model, 
                                                detector_backend="skip"
                                            )[0]["embedding"]
                                        )
                        torch.save(embed, f"{self.embed_path}/{i}_person {self.unique_person_counter}.pt")
                        self.unique_person_counter += 1
        logging.info("Done!")
    
    def compare_embed(
        self,
        embed_source: torch.tensor,
        file_type: str = "pt", 
        threshold: float =0.97
    ) -> Union[bool, str]:
        embeds = glob.glob(self.embed_path + f"/*.{file_type}")
        for embed in embeds: # aku hilangin enumerate
            embed_target = torch.load(embed)
            if cos_sim(embed_source, embed_target) > threshold:
                return True, embed
        else:
            return False, None
    
    def create_dirs(
        self, 
        base_path: str
    ) -> tuple[str, str]:
        
        base_path = base_path
        output_path = os.path.join(base_path, "output/")
        embed_path = os.path.join(base_path, "embed")
        
        for p in [base_path, output_path, embed_path]:
            if not os.path.isdir(p):
                os.mkdir(p)
        
        return output_path, embed_path

if __name__ == "__main__":
    i = Individualize(
        imgs_path="./data/",
        base_path="./output/",
    )
    i.run()