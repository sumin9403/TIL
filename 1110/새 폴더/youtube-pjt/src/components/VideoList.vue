<template>
  <div>
    <ul>
    <VideoListItem
    v-for="video in videos"
    :key="video.etag"
    :video="video"
    @select-video="selectVideo"
     />
  </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
    name:'VideoList',
    components: {
        VideoListItem,
    },
    methods:{
      selectVideo(video) {
        // console.log('select video', video)
        this.$emit('select-video', video)
      }
    },
    props:{
      videos: Array
    }

}
</script>

<style>

</style>