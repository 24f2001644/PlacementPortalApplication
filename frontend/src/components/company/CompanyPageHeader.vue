<template>

<div class="page-header">

    <div>

        <h2>

            {{ title }}

        </h2>

        <p>

            {{ subtitle }}

        </p>

    </div>

    <slot />

</div>

</template>

<script setup>

defineProps({

    title:String,

    subtitle:String

})

</script>

<style scoped>

.page-header{

display:flex;

justify-content:space-between;

align-items:center;

margin-bottom:30px;

}

.page-header h2{

font-size:30px;

font-weight:700;

color:#0F172A;

margin-bottom:6px;

}

.page-header p{

color:#64748B;

margin:0;

font-size:15px;

}

@media(max-width:768px){

.page-header{

flex-direction:column;

align-items:flex-start;

gap:15px;

}

}

</style>