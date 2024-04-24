### Word Frequency Analysis using Docker

this for stop word removal, and word frequency analysis using Python.

### How to build the image?

```sh
$ docker build -t word-frequency-analysis .
```

### How to create and run the container

```sh
$ docker container run -it --name word-frequency word-frequency-analysis:latest
```
