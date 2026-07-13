<template>

<div class="container mt-4">

<div class="card shadow">

<div class="card-header bg-dark text-white">

<h3>Portal Settings</h3>

</div>

<div class="card-body">

<div class="form-check form-switch mb-3">

<input

class="form-check-input"

type="checkbox"

v-model="registration"

>

<label class="form-check-label">

Student Registration Enabled

</label>

</div>

<div class="form-check form-switch mb-3">

<input

class="form-check-input"

type="checkbox"

v-model="companies"

>

<label class="form-check-label">

Company Registration Enabled

</label>

</div>

<button

class="btn btn-primary"

@click="save"

>

Save Settings

</button>

</div>

</div>

</div>

</template>

<script setup>

import {ref} from "vue"

const registration=ref(true)

const companies=ref(true)

function save(){

alert("Settings Saved")

}

</script>