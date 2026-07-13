<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
    <div class="container-fluid">

      <router-link class="navbar-brand fw-bold" to="/">
        Placement Portal
      </router-link>

      <button
        class="navbar-toggler"
        data-bs-toggle="collapse"
        data-bs-target="#navbar">

        <span class="navbar-toggler-icon"></span>

      </button>

      <div
        class="collapse navbar-collapse"
        id="navbar">

        <ul class="navbar-nav ms-auto align-items-center">

          <li class="nav-item me-3">

            <span class="text-white">

              Welcome {{ role }}

            </span>

          </li>

          <li class="nav-item">

            <button
              class="btn btn-light btn-sm"
              @click="logout">

              Logout

            </button>

          </li>

        </ul>

      </div>

    </div>
  </nav>
</template>

<script setup>

import { computed } from "vue";

import { useRouter } from "vue-router";

import { useAuthStore } from "../../stores/auth";

const authStore = useAuthStore();

const router = useRouter();

const role = computed(() => authStore.role || "Guest");

function logout() {

  authStore.logout();

  router.push("/login");

}

</script>