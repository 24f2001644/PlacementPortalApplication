<template>

<Navbar/>

<div class="d-flex">

<Sidebar/>

<div
class="flex-grow-1
p-4">

<router-view/>

</div>

</div>

<Footer/>

</template>

<script setup>

import Navbar from "../components/common/Navbar.vue";

import Sidebar from "../components/common/Sidebar.vue";

import Footer from "../components/common/Footer.vue";

</script>