<template>
  <div class="container mt-5" style="max-width:700px">

    <div class="card shadow">

      <div class="card-header bg-success text-white">
        <h3>Company Registration</h3>
      </div>

      <div class="card-body">

        <form @submit.prevent="registerCompany">

          <div class="mb-3">
            <label class="form-label">Company Name</label>
            <input
              v-model="company.company_name"
              class="form-control"
              required
            >
          </div>

          <div class="mb-3">
            <label class="form-label">Email</label>
            <input
              type="email"
              v-model="company.email"
              class="form-control"
              required
            >
          </div>

          <div class="mb-3">
            <label class="form-label">Password</label>
            <input
              type="password"
              v-model="company.password"
              class="form-control"
              required
            >
          </div>

          <div class="mb-3">
            <label class="form-label">Industry</label>
            <input
              v-model="company.industry"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">Location</label>
            <input
              v-model="company.location"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">Website</label>
            <input
              v-model="company.website"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">HR Name</label>
            <input
              v-model="company.hr_name"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">HR Email</label>
            <input
              type="email"
              v-model="company.hr_email"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">HR Phone</label>
            <input
              v-model="company.hr_phone"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">Description</label>

            <textarea
              rows="4"
              class="form-control"
              v-model="company.description"
            ></textarea>

          </div>

          <button
            class="btn btn-success w-100"
          >
            Register Company
          </button>

        </form>

      </div>

    </div>

  </div>
</template>

<script setup>

import { reactive } from "vue"

import { useRouter } from "vue-router"

import { registerCompany as registerCompanyApi } from "../../services/auth"

const router = useRouter()

const company = reactive({

    company_name: "",

    email: "",

    password: "",

    industry: "",

    location: "",

    website: "",

    hr_name: "",

    hr_email: "",

    hr_phone: "",

    description: ""

})

async function registerCompany(){

    try{

        await registerCompanyApi(company)

        alert(
            "Registration successful. Waiting for admin approval."
        )

        router.push("/login")

    }

    catch (error) {
    console.log(error)
    console.log(error.response)

    alert(
        error.response?.data?.message ||
        error.message ||
        "Registration failed"
    )
}

}

</script>