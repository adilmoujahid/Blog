# My Personal Blog README

This README provides instructions on how to set up, run, and deploy my personal blog using the Anaconda distribution of Python 3.8 and the Pelican static site generator. The blog is deployed on GitHub Pages.

## Setup

### 1. Create a conda environment

To create a new conda environment named `blog` with Python 3.8, run the following command:

```bash
conda create -n blog python=3.8
```

Activate the newly created environment:

```bash
conda activate blog
```

### 2. Install dependencies
Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Writing content and running the blog locally

After writing new posts, generate the output using the following command:

```bash
make html
```

To run the blog locally, use this command:

```bash
make serve
```

### Deploying the blog on GitHub Pages

Follow these steps to deploy the blog:


#### 1. Create the HTML pages

Generate the output and commit your changes:

```bash
make html
git add --all
git commit -m "Your commit message"
```

Import the output to the ```gh-pages``` branch:

```bash
ghp-import output
```

#### 2. Deploy the blog

Push your changes to the ```gh-pages``` branch on GitHub:

```bash
git push git@github.com:yourusername/yourusername.github.io.git gh-pages:master
```

In case you need to force push, use the ```-f``` flag:

```bash
git push -f git@github.com:yourusername/yourusername.github.io.git gh-pages:master
```

#### 3. Version control of both master branches

Finally, push your changes to the master branch:

```bash
git push origin master
```
Your blog should now be live on GitHub Pages.



