<script setup>

defineProps({

title:String,

icon:String,

route:String

})

</script>

<template>

<router-link

:to="route"

class="action-card"

>

<i :class="icon"></i>

<h5>

{{ title }}

</h5>

</router-link>

</template>

<style scoped>

.action-card{

display:flex;

flex-direction:column;

align-items:center;

justify-content:center;

padding:30px;

background:white;

border-radius:18px;

text-decoration:none;

color:#1e293b;

box-shadow:0 10px 30px rgba(0,0,0,.08);

transition:.3s;

}

.action-card:hover{

transform:translateY(-8px);

background:#4F46E5;

color:white;

}

.action-card i{

font-size:35px;

margin-bottom:10px;

}

</style>