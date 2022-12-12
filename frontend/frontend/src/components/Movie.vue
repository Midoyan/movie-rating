<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-12">
        <h1>{{ movie.title }}</h1>
        <p>
          <span>Released in {{ movie.year }}</span>
        </p>
      </div>
      <div class="col-6">
        <img :src="movie.poster" />
      </div>
      <div class="col-6">
        <p><span class="film-prop">Plot: </span>{{ movie.plot }}</p>
        <p><span class="film-prop">Genre: </span>{{ movie.genre }}</p>
        <p><span class="film-prop">Runtime: </span>{{ movie.runtime }}</p>
        <p><span class="film-prop">Release date: </span>{{ movie.date }}</p>
        <p><span class="film-prop">Director: </span>{{ movie.director }}</p>
        <p><span class="film-prop">Writer: </span>{{ movie.writer }}</p>
        <p><span class="film-prop">Actors: </span>{{ movie.actors }}</p>
        <p><span class="film-prop">Country: </span>{{ movie.country }}</p>
        <p><span class="film-prop">Awards: </span>{{ movie.awards }}</p>
        <p><span class="film-prop">Box office: </span>{{ movie.box_office }}</p>
        <p>
          <span class="film-prop">IMDB rating: </span>{{ movie.imdb_rating }}
        </p>
        <p><span class="film-prop">IMDB votes: </span>{{ movie.imdb_votes }}</p>
        <p v-if="Object.keys(evalRating).length !== 0">
          <span class="film-prop">Our platform rating: </span
          >{{ evalRating.mark }} ({{ evalRating.value }})
        </p>
      </div>
      <div class="col-12">
        <h2>Rate this film</h2>
        <p>Click the button below with the rating that is closest to yours</p>
        <div class="buttons">
          <button
            class="btn"
            :class="[rating.classes]"
            type="button"
            v-for="(rating, index) in ratings"
            :key="index"
            @click="rateMovie(index)"
          >
            {{ rating.text }}
          </button>
        </div>
        <h2 class="mt-4">Recent votes</h2>
        <div v-if="!votes.length">Nobody rated this film</div>
        <div v-if="votes.length">
          <div v-for="(vote, index) in votes" :key="index">
            <p>
              {{ index + 1 }}) Mark "{{ ratings[vote.mark_id].text }}" has been
              given on {{ vote.date }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieComponent",
  data() {
    return {
      msg: "Hello, this is Movie",
      movie: [],
      votes: [],
      evalRating: {},
      ratings: [
        { text: "Very bad", classes: "btn-danger dark-red" },
        { text: "Bad", classes: "btn-danger" },
        { text: "Somewhat bad", classes: "btn-danger orange" },
        { text: "Fair", classes: "btn-warning" },
        { text: "Somewhat good", classes: "btn-success olive" },
        { text: "Good", classes: "btn-success" },
        { text: "Very good", classes: "btn-success green" },
      ],
    };
  },
  async created() {
    await this.getMovie();
    console.log(this.movie);
    await this.getMovieVotes();
    console.log(this.votes);
    await this.getMovieRating();
    console.log(this.evalRating);
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
    async getMovie() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getMovie/" + this.$route.params.id,
        "get"
      );
      this.movie = await response.json();
    },
    async getMovieVotes() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getMovieVotes/" + this.$route.params.id,
        "get"
      );
      this.votes = await response.json();
    },
    async getMovieRating() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getMovieRating/" + this.$route.params.id,
        "get"
      );
      this.evalRating = await response.json();
    },
    async rateMovie(btn_id) {
      const vote = {
        film_id: this.$route.params.id,
        mark_id: btn_id,
      };
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/vote",
        "post",
        JSON.stringify(vote)
      );
      const temp = await response.json();
      console.log(temp);
      await this.getMovie();
      await this.getMovieVotes();
      await this.getMovieRating();
    },
  },
};
</script>
