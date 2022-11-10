<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
      <div class="shadow p-4 mb-6 bg-body rounded mx-auto" style="width: 50%" >
        <h2>예약 페이지</h2>
        <br>
        <h3>시간 선택</h3>
            
        <div class="container text-center">
          <div class="row row-cols-8">
            <div v-for="(time, idx) in times" :key="idx" class="col"
            @click="choice(time)" :class="{ cchoiced : time.selected }">
                {{ time['hour'] }}:{{ time['minute'] }}
            </div>     
          </div>
        </div>
        <hr>
        <h4>선택시간: <span v-if="selected.length"><span v-for="(elem, ind) in selected" :key=ind>{{ elem }} </span></span></h4>
      </div>


      
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      times: []
    }
  },
  computed: {
    selected() {
      const rst = this.times.filter((time) => {
          return time.selected
      }).map(time => {
        return String(time.hour)+':'+String(time.minute)
      })
      return rst
    }
  },
  methods: {
    choice(time){
      time.selected = !time.selected
      if (this.selected.length > 5) {
        time.selected = !time.selected
        alert('5타임까지만 신청할 수 있습니다.')
      } 
    }
  },
  created(){
    for (let i=0; i<24; i++){
      for (const n of ['00','30']){
        this.times.push({
          'hour': (i>=10) ? String(i) : '0' + String(i),
          'minute':n,
          'selected':false,}
          )
      }
    }
    console.log(this.times)
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
.cchoiced {
  background-color: #658dc63d;
}
</style>
