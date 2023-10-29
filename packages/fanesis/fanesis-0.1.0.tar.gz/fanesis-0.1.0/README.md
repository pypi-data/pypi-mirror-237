# Facial Network Analysis

![diagram](/img/diagram.png)

Fanesis is a Facial Network Analysis tool that analyzes the faces and behaviors of individuals in a group and creates a visual representation of their relationships. Fanesis uses computer vision and machine learning techniques to detect the emotions and interactions of each individual. It then creates two types of associations: group-based and emotion-based. Group-based associations show how individuals are connected within the group, such as who knows whom, who is close to whom, and who is influential to whom. Emotion-based associations show how individuals feel about each other, such as who likes whom, who dislikes whom, and who is neutral to whom. Fanesis provides insights into the dynamics and characteristics of the group, which can be useful for various applications such as social network analysis, group psychology, and team building.

![gba](/img/gba.png)
Here is an example output from a very small dataset of images. We are presenting the results from a different embedding model. This allows us to analyze which person is more popular in the known dataset.

> [!WARNING]
> The quality of the generated network depends on the quality of the embedding model.

## Installation

## Usage

Using the individual classes

```python
from fanesis import Individualize, Grouping, Visualize

imgs_path = "./data/"
base_path = "./output/"
output_path = "./output/output/"

i = Individualize(imgs_path, base_path)
i.run()

g = Grouping(output_path)
df = g.run()

v = Visualize(output_path)
v.visualize(df)
```

Using `FanesisPipeline`

```python
from fanesis import FanesisPipeline

imgs_path = "./data/"
base_path = "./output/"

pipeline = FanesisPipeline()
pipeline(imgs_path, base_path)
```
