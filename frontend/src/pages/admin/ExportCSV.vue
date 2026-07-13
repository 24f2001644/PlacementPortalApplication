<template>

<div class="container mt-4">

<div class="card shadow">

<div class="card-header bg-info text-white">

<h3>Export Data</h3>

</div>

<div class="card-body text-center">

<p>

Download placement reports in CSV format.

</p>

<button

class="btn btn-success me-3"

@click="exportStudents"

>

Export Students

</button>

<button

class="btn btn-primary me-3"

@click="exportApplications"

>

Export Applications

</button>

<button

class="btn btn-dark"

@click="exportCompanies"

>

Export Companies

</button>

</div>

</div>

</div>

</template>

<script setup>

function exportStudents(){

alert("Later connect CSV API")

}

function exportApplications(){

alert("Later connect CSV API")

}

function exportCompanies(){

alert("Later connect CSV API")

}

</script>