```vue
<template>
  <div class="container-fluid min-vh-100 d-flex align-items-center justify-content-center bg-light">
    <div class="card shadow-lg p-4" style="width: 420px;">
      <div class="text-center mb-4">
        <h2 class="fw-bold">Placement Portal</h2>
        <p class="text-muted">Login to your account</p>
      </div>

      <div
        v-if="errorMessage"
        class="alert alert-danger"
      >
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleLogin">

        <div class="mb-3">
          <label class="form-label">Email</label>

          <input
            type="email"
            class="form-control"
            v-model="form.email"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Password</label>

          <input
            type="password"
            class="form-control"
            v-model="form.password"
            required
          >
        </div>

        <div class="mb-4">
          <label class="form-label">Login As</label>

          <select
            class="form-select"
            v-model="form.role"
            required
          >
            <option value="">Select Role</option>
            <option value="STUDENT">Student</option>
            <option value="COMPANY">Company</option>
            <option value="ADMIN">Admin</option>
          </select>
        </div>

        <button
          class="btn btn-primary w-100"
          :disabled="loading"
        >
          <span
            v-if="loading"
            class="spinner-border spinner-border-sm me-2"
          ></span>

          {{ loading ? "Logging in..." : "Login" }}
        </button>

      </form>

      <hr>

      <div class="text-center">

        <router-link
          to="/register/student"
          class="d-block mb-2"
        >
          Register as Student
        </router-link>

        <router-link
          to="/register/company"
        >
          Register as Company
        </router-link>

      </div>

    </div>
  </div>
</template>

<script setup>

import { reactive, ref } from "vue";

import { useRouter } from "vue-router";

import { useAuthStore } from "../../stores/auth";

const router = useRouter();

const auth = useAuthStore();

const loading = ref(false);

const errorMessage = ref("");

const form = reactive({

  email: "",

  password: "",

  role: ""

});

async function handleLogin() {

  loading.value = true;

  errorMessage.value = "";

  try {

    await auth.login(form);

    if (auth.role === "ADMIN") {

      router.push("/admin/dashboard");

    }

    else if (auth.role === "COMPANY") {

      router.push("/company/dashboard");

    }

    else {

      router.push("/student/dashboard");

    }

  }

  catch (error) {

    if (error.response) {

      errorMessage.value =

        error.response.data.message;

    }

    else {

      errorMessage.value =

        "Unable to connect to server.";

    }

  }

  finally {

    loading.value = false;

  }

}

</script>
```
