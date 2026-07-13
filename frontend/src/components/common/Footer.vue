<template>

<footer
    class="bg-dark
           text-white
           text-center
           py-3">

    © {{ year }}

    Placement Portal Application

</footer>

</template>

<script setup>

const year = new Date().getFullYear();

</script>