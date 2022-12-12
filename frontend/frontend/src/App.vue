<script>
import MyHeader from "./components/Header.vue";

export default {
  components: {
    MyHeader,
  },
};
</script>

<template>
  <MyHeader />
  <router-view />
</template>

<style>
nav a.router-link-exact-active {
  color: #42b983;
}
.star-icon {
  font-size: 28px;
  height: 0.8em;
  width: 1em;
  margin-right: 0.15em;
}
.imdb-mark {
  font-weight: bold;
}
.card-title {
  font-size: 23px;
  margin-top: 15px;
  text-align: center;
  padding-left: 5px;
  padding-right: 5px;
  padding-bottom: 10px;
}
.card-ratings {
  padding-left: 5px;
  padding-right: 5px;
}

.card-shadow:hover {
  box-shadow: 0 3px 1px -2px rgb(0 0 0 / 20%), 0 2px 2px 0 rgb(0 0 0 / 14%),
    0 1px 5px 0 rgb(0 0 0 / 12%);
  transition-duration: 0.5s;
}

.card-poster {
  height: 454px;
}

.card-links {
  color: inherit; /* blue colors for links too */
  text-decoration: inherit; /* no underline */
}

.film-prop {
  font-weight: bold;
}

.buttons .btn {
  width: 160px;
  height: 50px;
  margin-right: 20px;
}

.red {
  background: red;
  border-color: red;
}

.btn.orange {
  background: #ff8800;
  border-color: #ff8800;
}

.btn.olive {
  background: olive;
  border-color: olive;
}

.btn.green {
  background: green;
  border-color: green;
}

.btn.dark-red {
  background: darkred;
  border-color: darkred;
}
</style>
