<template>
  <v-container class="fill-height">
    <v-row
      justify="center"
      align="center"
    >
      <v-col class="">
        <div>
            <hooper ref="carousel" :vertical="true" class="video" :itemsToShow="1" :centerMode="true" :autoPlay="true" :playSpeed="playSpeed" @slide="updateVideo">
              <slide v-for="url in urls" :key="url">
                <Embed :params="{ autoplay: 0 }" :src="url"/>
              </slide>
            </hooper>
            <v-row>
            <v-col class="text-align-right">
              <p class="text-right">
                <button class="pr-5" @click.prevent="videoPrev"><v-icon x-large color="grey">mdi-arrow-up-bold</v-icon></button>
                <button @click.prevent="videoNext"><v-icon x-large color="red">mdi-arrow-down-bold</v-icon></button>
              </p>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { Hooper, Slide } from 'hooper';
import Embed from './Embed';
import axios from 'axios';
import Config from '../config';

import 'hooper/dist/hooper.css';
  export default {
    name: 'Videos',
    components: {
      Hooper,
      Slide,
      Embed
    },
    data: () => ({
      urls: [],
      playSpeed: Config.videoPlaySpeed // 30secs
    }),
    created() {
      this.videos();
    },
    methods: {
      videoPrev() {
        this.$refs.carousel.slidePrev();
      },
      videoNext() {
        this.$refs.carousel.slideNext();
      },
      updateVideo(payload) {
        this.myCarouselData = payload.currentSlide;
      },
      async videos() {
        const videos = await axios({
          method: 'GET',
          url: `${Config.apiBaseUrl}/api/videos`
        })

        this.urls = videos.data;
      }
    }
  }
</script>
<style scoped>
.video {
  width: 90%; 
  height: 450px; 
  padding-top:10px
}
</style>
