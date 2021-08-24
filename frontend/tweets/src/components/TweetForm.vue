<template>
  <div id="container">
    <div id="box">
      <form @submit.prevent="onSubmit" class="form-inline">
          <label>Name</label>
          <input v-model="name" placeholder="Name" required="required">
          <label>Tweet</label>
          <textarea v-model="tweet" placeholder="Write you thoughts" required="required"></textarea>
          &nbsp;&nbsp;<button type="submit">Submit</button>
      </form>
    </div>
    <br><br><br>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Tweet</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{item.username}}</td>
          <td>{{item.tweet_message}}</td>
          <td>{{item.created_at}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  username: 'TweetForm',
  created(){
    this.getTweets()
  },
  
  data() {
      return {
        name: '',
        tweet: '',
        items:[]
      }
  },
  methods: {
    onSubmit() {
      if(this.tweet.length > 51){
       alert("Tweet should less then 50 character");
       return;
      
      }
    
      this.axios.post('/api/tweet/',{username: this.name,tweet_message:this.tweet})
      
      .then(res => {
        this.name = ""
        this.tweet = ""
        this.getTweets()
        console.log(res);
      })
      
      .catch(error => {
        console.log(error)
      })
     
    },
    
    getTweets() {
        this.axios.get('/api/tweet/')
        .then(res => {
            this.items = res.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
<style >
  #box{
    border: 3px solid #38383b;
    padding: 10px;
  }
  #container {
    justify-content: center;
    display: grid;
  }

  table {
    font-family: 'Open Sans', sans-serif;
    width: 750px;
    border-collapse: collapse;
    border: 3px solid #38383b;
    margin: 10px 10px 0 10px;
  }

  table th {
    text-transform: uppercase;
    text-align: left;
    background: #31fff5;
    color: rgb(8, 8, 8);
    padding: 8px;
    min-width: 30px;
  }

  table td {
    text-align: left;
    padding: 8px;
    border-right: 2px solid #92d0d3;
  }
  table td:last-child {
    border-right: none;
  }
  table tbody tr:nth-child(2n) td {
    background: #c9ecf1;
  }

  .form-inline {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
  }

  .form-inline label {
    margin: 5px 10px 5px 0;
  }

  .form-inline input {
    vertical-align: middle;
    margin: 5px 10px 5px 0;
    padding: 10px;
    background-color: rgb(255, 255, 255);
    border: 1px solid #ddd;
  }

  .form-inline button {
    padding: 10px 20px;
    background-color: rgb(39, 255, 10);
    border: 1px solid rgb(0, 0, 0);
    color: rgb(12, 12, 12);
  }

  .form-inline button:hover {
    background-color: rgb(12, 100, 0);
  }
  
</style>