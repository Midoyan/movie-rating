<template>
  <div class="container">
    <div class="row">
      <div class="col-12 mt-5">
        <h1>Rate the movie</h1>
        <p>Please select a movie to rate it.</p>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col-3" v-for="(movie, index) in movies" :key="index">
        <router-link
          :to="{ name: 'Movie', params: { id: movie.id } }"
          class="card-links"
        >
          <div class="d-flex flex-column card-shadow">
            <img class="card-poster" :src="movie.poster" />
            <div class="mt-3 d-flex justify-content-between card-ratings">
              <div class="d-flex align-content-center">
                <img class="star-icon" src="../assets/star.svg" />
                <span class="imdb-mark">IMDB: {{ movie.imdb_rating }}</span>
              </div>
              <span class="imdb-mark ml-3">Users mark: {{ movie.rating }}</span>
            </div>
            <span class="card-title">{{ movie.title }}</span>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CarEvaluation",
  data() {
    return {
      movies: [],
    };
  },
  async created() {
    await this.getMovies();
    console.log(this.movies);
  },
  methods: {
    async sendRequest(url, method, data) {
      const myHeaders = new Headers({
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
      });

      const response = await fetch(url, {
        method: method,
        headers: myHeaders,
        body: data,
      });

      return response;
    },
    async getMovies() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getMovies",
        "get"
      );
      this.movies = await response.json();
    },
  },
};
</script>
