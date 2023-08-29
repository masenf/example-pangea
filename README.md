# Formation of the continents

This is just for demo purposes, please see original sources:

* https://www.youtube.com/watch?app=desktop&v=OGdPqpzYD4o
* https://apl.maps.arcgis.com/apps/MapJournal/index.html?appid=3c784abfe153444ca7bda3f53cbeef33&adumkts=social&utm_source=social&aduc=social&adum=external&aduca=social_technical&adusf=youtube&adut=253268ed-a579-4504-add2-9917c3a9b20c
* [Acknowledgements](https://apl.maps.arcgis.com/apps/MapJournal/index.html?appid=3c784abfe153444ca7bda3f53cbeef33&adumkts=social&utm_source=social&aduc=social&adum=external&aduca=social_technical&adusf=youtube&adut=253268ed-a579-4504-add2-9917c3a9b20c)
* The data used to create the slides developed by [Prof. Christopher R. Scotese, PALEOMAP Project.](http://www.scotese.com)

## Video extracted from youtube:

```
yt-dlp 'https://www.youtube.com/watch?app=desktop&v=OGdPqpzYD4o'
```

## Frames extracted via FFMPEG

```
ffmpeg -ss 00:07 -i Continental\ Drift\ from\ Pangea\ to\ Today\ \[OGdPqpzYD4o\].mp4 -r 0.75 pangea/image-%03d.png
```

## Frames processed with PIL

```
python process.py
```
