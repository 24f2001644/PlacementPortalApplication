<template>

<nav>

<ul class="pagination justify-content-center">

<li
class="page-item"
:class="{disabled:page===1}">

<button
class="page-link"
@click="$emit('prev')">

Previous

</button>

</li>

<li class="page-item active">

<span class="page-link">

{{ page }}

</span>

</li>

<li class="page-item">

<button
class="page-link"
@click="$emit('next')">

Next

</button>

</li>

</ul>

</nav>

</template>

<script setup>

defineProps({

page:Number

})

defineEmits([

"next",

"prev"

])

</script>