<template>
  <div class="container">
    <li>
        <ul v-for="beer in beers" :key="beer.id">
            <div>
                <h3>{{ beer.name }}</h3>
                <img :src="beer.image" alt="beer_img">
                <p>mark: {{ beer.mark }}</p>
                <p>price: {{ beer.price }}</p>
            </div>
        </ul>
    </li>
    <button v-on:click="getBeers" type="button" class="btn btn-primary">Load more</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      beers: [],
    };
  },
  methods: {
    getBeers() {
      console.log('Get beers');
      const path = `${process.env.VUE_APP_API_URL}/beers`;
      axios.get(path)
        .then((res) => {
          this.beers = res.data.results;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getBeers();
  },
};
</script>
