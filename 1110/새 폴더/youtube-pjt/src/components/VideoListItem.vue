<template>
  <li @click="selectVideo">
    <img :src="thumbnailUrl" >
    <span>{{ videoTitle|stringUnescape }}</span>
  </li>
</template>

<script>
import _ from 'lodash'
export default {
    name:'VideoListItem',
    props:{
      video: Object
    },
    methods:{
      selectVideo() {
        this.$emit('select-video', this.video)
      }
    },
    computed:{
      thumbnailUrl() { return this.video.snippet.thumbnails.default.url },
      videoTitle() {
        return this.video.snippet.title
      }
    },
    filters : {
      stringUnescape(rawText) {
        return _.unescape(rawText)
      }
    }

}
</script>

<style>

</style>