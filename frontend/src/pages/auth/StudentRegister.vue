<template>
  <div class="container py-5">
    <div class="row justify-content-center">

      <div class="col-lg-9">

        <div class="card shadow">

          <div class="card-header bg-primary text-white">
            <h3 class="mb-0">Student Registration</h3>
          </div>

          <div class="card-body">

            <div
              v-if="errorMessage"
              class="alert alert-danger"
            >
              {{ errorMessage }}
            </div>

            <div
              v-if="successMessage"
              class="alert alert-success"
            >
              {{ successMessage }}
            </div>

            <form @submit.prevent="registerStudentForm">

              <div class="row">

                <div class="col-md-6 mb-3">
                  <label class="form-label">Full Name</label>

                  <input
                    type="text"
                    class="form-control"
                    v-model="form.full_name"
                    required
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label class="form-label">Roll Number</label>

                  <input
                    type="text"
                    class="form-control"
                    v-model="form.roll_number"
                    required
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label>Email</label>

                  <input
                    type="email"
                    class="form-control"
                    v-model="form.email"
                    required
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label>Password</label>

                  <input
                    type="password"
                    class="form-control"
                    v-model="form.password"
                    required
                  >
                </div>

                <div class="col-md-4 mb-3">
                  <label>Graduation Year</label>

                  <input
                    type="number"
                    class="form-control"
                    v-model="form.graduation_year"
                    required
                  >
                </div>

                <div class="col-md-4 mb-3">
  <label>Current Year</label>

  <select
    class="form-control"
    v-model="form.year"
    required
  >
    <option value="" disabled>Select Current Year</option>
    <option :value="1">1st Year</option>
    <option :value="2">2nd Year</option>
    <option :value="3">3rd Year</option>
    <option :value="4">4th Year</option>
  </select>
</div>

                <div class="col-md-4 mb-3">
                  <label>CGPA</label>

                  <input
                    type="number"
                    step="0.01"
                    class="form-control"
                    v-model="form.cgpa"
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label>10th Percentage</label>

                  <input
                    type="number"
                    step="0.01"
                    class="form-control"
                    v-model="form.tenth_marks"
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label>12th Percentage</label>

                  <input
                    type="number"
                    step="0.01"
                    class="form-control"
                    v-model="form.twelfth_marks"
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label>Course</label>

                  <input
                    type="text"
                    class="form-control"
                    v-model="form.course"
                  >
                </div>

                <div class="col-md-6 mb-3">

  <label>Branch</label>

  <select
    class="form-select"
    v-model="form.branch"
    required
  >

    <option disabled value="">
      Select Branch
    </option>

    <option
      v-for="branch in branches"
      :key="branch"
      :value="branch"
    >
      {{ branch }}
    </option>

  </select>

</div>

                <div class="col-md-6 mb-3">
                  <label>Date of Birth</label>

                  <input
                    type="date"
                    class="form-control"
                    v-model="form.dob"
                  >
                </div>

                <div class="col-md-6 mb-3">
                  <label>Phone</label>

                  <input
                    type="text"
                    class="form-control"
                    v-model="form.phone"
                  >
                </div>

                <div class="col-12 mb-3">
                  <label>Address</label>

                  <textarea
                    class="form-control"
                    rows="3"
                    v-model="form.address"
                  ></textarea>
                </div>

                <div class="col-12 mb-3">
                  <label>Skills</label>

                  <textarea
                    class="form-control"
                    rows="3"
                    placeholder="Java, Python, SQL, Vue..."
                    v-model="form.skills"
                  ></textarea>
                </div>

                <div class="col-12 mb-4">
                  <label>Resume (PDF)</label>

                  <input
                    type="file"
                    class="form-control"
                    accept=".pdf,.doc,.docx"
                    @change="handleResume"
                  >
                </div>

              </div>

              <button
                class="btn btn-primary w-100"
                :disabled="loading"
              >

                <span
                  v-if="loading"
                  class="spinner-border spinner-border-sm me-2"
                ></span>

                {{ loading ? "Registering..." : "Register" }}

              </button>

            </form>

          </div>

        </div>

      </div>

    </div>
  </div>
</template>

<script setup>

import { reactive, ref } from "vue";

import { useRouter } from "vue-router";

import { registerStudent } from "../../services/auth";

const router = useRouter();

const loading = ref(false);

const errorMessage = ref("");

const successMessage = ref("");

let resume = null;


const branches = [

  "CSE",

  "IT",

  "AIML",

  "CSDS",

  "ECE",

  "EEE",

  "ME",

  "CE"

];

const form = reactive({

  full_name: "",

  roll_number: "",

  email: "",

  password: "",

  graduation_year: "",

  year: "",

  cgpa: "",

  tenth_marks: "",

  twelfth_marks: "",

  course: "",

  branch: "",

  dob: "",

  phone: "",

  address: "",

  skills: ""

});

function handleResume(event) {

  resume = event.target.files[0];

}

async function registerStudentForm() {

  loading.value = true;

  errorMessage.value = "";

  successMessage.value = "";

  try {

    const formData = new FormData();

    Object.keys(form).forEach(key => {

      formData.append(key, form[key]);

    });

    if (resume) {

      formData.append("resume", resume);

    }

    await registerStudent(formData);

    successMessage.value =
      "Registration successful. Redirecting to login...";

    setTimeout(() => {

      router.push("/login");

    }, 1500);

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