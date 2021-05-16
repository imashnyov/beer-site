<template>
  <div class="container">
    <li>
      <ul v-for="beer in beers" :key="beer.id">
        <div>
          <h3>{{ beer.name }}</h3>
          <img :src="beer.image" alt="beer_img" />
          <p>mark: {{ beer.mark }}</p>
          <p>price: {{ beer.price }}</p>
        </div>
      </ul>
    </li>
    <p>{{ count }} / {{ maxCount }}</p>
    <button v-on:click="getBeers" v-if="count < maxCount"
    type="button" class="btn btn-primary">
      Load more
    </button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      beers: [],
      count: 0,
      maxCount: 0,
    };
  },
  methods: {
    getBeers() {
      console.log('Get beers');
      const path = `${process.env.VUE_APP_API_URL}/beers`;
      const params = { offset: this.count };
      axios
        .get(path, { params })
        .then((res) => {
          this.beers = this.beers.concat(res.data.results);
          this.maxCount = res.data.count;
          this.count += res.data.results.length;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getBeers();
  },
};
</script>
