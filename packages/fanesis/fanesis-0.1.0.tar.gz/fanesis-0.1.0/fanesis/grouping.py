import glob
import pandas as pd

class Grouping:
    def __init__(
        self,
        output_path: str,
    ) -> None:
        self.output_path = output_path

    
    def run(self) -> pd.DataFrame:
        person_occurances = self.get_person_occurance(self.output_path)
        shared_positions = self.find_shared_positions(person_occurances)
        association_df = pd.DataFrame(shared_positions, columns=["person1", "person2", "position"])
        association_df.drop(["position"], axis=1, inplace=True)
        association_df["value"] = 1
        association_df = association_df.groupby(["person1","person2"], sort=False, as_index=False).sum()
        
        return association_df
        
    def get_person_occurance(
        self, 
        output_path: str,
    ) -> dict[str, list[str]]:
        people = glob.glob(f"{output_path}/*")
        person_occurances = {}
        for person in people:
            person_i = glob.glob(person + "/*")
            person_i = [i.split("\\")[-1] for i in person_i]
            person_i = [i.split("_")[0] for i in person_i]
            current_person = person.split("\\")[-1]
            person_occurances[current_person] = person_i
        
        return person_occurances
    
    def find_shared_positions(
        self,
        people_positions
    ) -> list[list[str, str, str]]:
        shared_positions = []
        already_processed = set()

        for person1, positions1 in people_positions.items():
            for person2, positions2 in people_positions.items():
                if person1 != person2 and (person2, person1) not in already_processed:
                    common_positions = set(positions1) & set(positions2)

                    for position in common_positions:
                        shared_positions.append([person1, person2, int(position)])
                        already_processed.add((person1, person2))

        return shared_positions

if __name__ == "__main__":
    output_path = "./output/output/"
    grouping = Grouping(output_path)
    df = grouping.run()