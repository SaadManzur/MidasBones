# Overview
When creating this repositories there are at least 4 different (to my best knowledge) pose estimation datasets that support 2D-3D correspondences. With many more if only account for 2D annotations alone. As part of my research going through all of these datasets and working with different joint arrangements and selections is often annoying for me (I like things automated). The problem is that these datasets, has their own way of annotating and arranging different joints. This repository is created as a common interface among these datasets. ***One interface to rule them all.***

The idea is that whenever you are introducing a new dataset, you just fill out a ***json meta*** file and the code will automatically parse and build the skeleton. After this, all you have to do is pick the joint names and it will be able to give you the indices you need to pick along with parent, left, and right joint set.

I will be contributing to this repository as much as possible, whenever I get some time to breathe.

# Command Line Arguments
```-dm, --dump-meta```
Dump a sample meta file, fill out this file rename it if you want. This filled out json can be used to generate the skeleton.

```-pm, --parse-meta```
Parse the filled out meta json and generate skeleton (pass the file path)

```-pj, --pick-joints```
Pick joints from a json file's array, the array will have the joint keys from the original meta file

```-pd, --plot-dummy```
Plot a dummy skeleton to show what joints are picked

```-ppj, --plot-picked-joints```
Plot dummy skeleton on picked joints