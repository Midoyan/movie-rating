import { createRouter, createWebHistory } from "vue-router";
import CarEvaluation from "../components/CarEvaluation.vue";
import Movie from "../components/Movie.vue";

const routes = [
  {
    path: "/",
    name: "CarEvaluation",
    component: CarEvaluation,
  },
  {
    path: "/movie/:id",
    name: "Movie",
    component: Movie,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
