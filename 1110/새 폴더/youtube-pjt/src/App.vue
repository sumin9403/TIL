<template>
  <div id="app">
    <h1 style="color:red;">Youtube Project</h1>
    
    <!-- 검색 창 -->
    <TheSearchBar
    @input-change="inputChange"
     />

    <div>
      <VideoDetail :video="selectedVideo" />
      <VideoList
      :videos="videos"
      @select-video="selectVideo"
      />
    </div>
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'App',
  data() {
    return {
      videos: null,
      selectedVideo: null,
    }
  },
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  methods:{
    inputChange(arg) {
      axios({
        url: 'https://www.googleapis.com/youtube/v3/search',
        // method 가 get일 때는 안 적어도 괜찮음
        method: 'get',
        params:{
          //필수 인자
          key: API_KEY,
          part: 'snippet',

          // 선택 옵션
          q: arg, // 검색어 담당
          type: 'video',
        }
      })
        .then(res => {
          this.videos = res.data.items
        })
        .catch(err => {
          console.log(err)
        })
    },
    selectVideo(video) {
      // console.log('select video', video.snippet.title)
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
