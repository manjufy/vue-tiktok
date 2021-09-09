# manju-vue-tiktoker

Simple WebApp to demo TikTok like videos.

Note: Default video playback is 30 seconds. This value can be changed from `src/config.videoPlaySpeed`

## Project setup

## API Setup

- Make sure to have Python 3.7.1 installed
- Have pip version pip 20.1.1 installed
- Install flask `pip install flask`
- Then `pip install -U flask-cors`

```
git clone https://github.com/manjufy/tiktoker-api.git
$ cd tiktoker-api
$ flask run

Head to http://localhost:5000
API to get list of videos http://localhost:5000/api/videos
```

## Web Client Setup

- Make sure to have node v12.0+ installed

```
git clone https://github.com/manjufy/manju-vue-tiktoker.git
$ cd manju-vue-tiktoker
$ npm install
$ npm run serve
Head to http://localhost:8080
```
