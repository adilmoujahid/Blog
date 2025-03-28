title: Fusion Bricks: Exploring Generative Art and LEGO Building
Slug: fusion-bricks

In this project, I aimed to explore the convergence of generative art, pixel art, and LEGO creations. To achieve this, I redeveloped my initial fxhash project, [Geometric Grid Fusion](https://www.fxhash.xyz/generative/24620), using Pico-8 and then chose several outputs to construct with LEGO bricks.

[PICO-8](https://www.lexaloffle.com/pico-8.php), created by Lexaloffle Games, is a virtual machine and game engine that features a 128x128 pixel display and utilizes a 16-color palette. Although I typically employ p5.js for my generative art projects, I decided to explore PICO-8 and its potential for generative art in this particular endeavor. Given that the LEGO board I used has a 32x32 pixel grid and a limited range of brick colors, I chose a black, white, and grey color palette. Furthermore, the generative piece needed to fit within a 32x32 board.

</br>

###The Algorithm

The PICO-8 program generates a random, abstract pattern composed of rectangles and lines in black, white, and grey colors.

The program begins with an empty 128x128 black canvas and divides it recursively into smaller rectangles of random sizes until a specified limit is reached. The width and height of the rectangles can be one of the following values: 64, 32, 16, or 8 pixels. This ensures that the final results can be seamlessly adapted to a 32x32 LEGO board.

<div style="display:block;margin:auto;height:75%;width:75%">
    <img src="/images/fusion-bricks/grids.png">
</div>

</br>

For each rectangle, the algorithm determines whether to draw smaller squares or lines within it. The colors, as well as the direction of the lines (horizontal or vertical), are also randomly decided. The sizes of squares and lines are chosen randomly, taking into account the size of the corresponding rectangle.

<div style="display:block;margin:auto;height:70%;width:70%">
    <img src="/images/fusion-bricks/rects-lines.png">
</div>

</br>

Below is a gif showcasing a few outputs of the PICO-8 generative algorithm, providing a glimpse into the range of abstract patterns and textures that the algorithm can generate. Each output is unique and showcases the unpredictable yet intriguing nature of generative art.

<div style="text-align:center;">
    <img src="/images/fusion-bricks/ggflego.gif" style="height:60%;width:60%">
</div>

</br>

You can find the source code in [this github repository](https://github.com/adilmoujahid/fusion-bricks-pico8).

### From Digital to Physical: Building the LEGO Art

After generating numerous abstract patterns through the PICO-8 algorithm, I selected two outputs that I found particularly compelling. The next stage of the project involved translating these digital designs into tangible LEGO constructions. I chose LEGO for this task because it offers a hands-on medium to interact with, and its grid-based nature pairs well with pixelated generative art.

The two selected designs were:

<div style="display:block;margin:auto;height:80%;width:80%">
    <img src="/images/fusion-bricks/selected_designs.png">
</div>
</br>

To facilitate the transition from digital to physical, I created a grid view of the selected designs, allowing me to calculate the exact number and sizes of bricks required for each design. With a detailed list in hand, I was then able to order the necessary bricks in the right quantities and colors. This step was essential to ensure a seamless building process, minimizing any potential disruptions due to a lack of specific bricks.

<div style="display:block;margin:auto;height:80%;width:80%">
    <img src="/images/fusion-bricks/blueprint.png">
</div>
</br>

Building the LEGO art is a straightforward process. With the bricks sorted by color and size, all that was needed was to follow the grid blueprint. I built the designs layer by layer, closely adhering to the outlined pattern.

<div style="display:block;margin:auto;height:60%;width:60%">
    <img src="/images/fusion-bricks/building_process.gif">
</div>
</br>
Here are the final LEGO constructions, a material manifestation of the digital abstract patterns generated by the PICO-8 algorithm:

<div style="display:block;margin:auto;height:60%;width:60%">
    <img src="/images/fusion-bricks/final_lego.jpeg">
</div>
</br>

This project showcased an intriguing fusion of generative art, pixel art, and LEGO building. Translating digital patterns into physical LEGO art was a rewarding process. It not only brought the designs to life but also added a new dimension of physical presence to the abstract patterns. This experiment has opened up new avenues for me to explore in the realm of generative art, and I look forward to creating more art in this fascinating intersection in the future.

<span data-sumome-listbuilder-embed-id="593f1f61fd137dfe732a80686197b429a62e5c6e6bd62242966f34199d064e47"></span>