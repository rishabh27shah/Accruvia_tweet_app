<template>
  <TweetForm />
</template>
<script>
import TweetForm from './components/TweetForm.vue'

export default {
  name: 'App',
  components: {
    TweetForm,
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
