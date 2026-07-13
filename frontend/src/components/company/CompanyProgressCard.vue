<template>

<div class="progress-card">

    <div class="d-flex justify-content-between">

        <h6>

            {{ title }}

        </h6>

        <strong>

            {{ value }}%

        </strong>

    </div>

    <small>

        {{ label }}

    </small>

    <div class="progress mt-3">

        <div

            class="progress-bar bg-success"

            :style="{

                width:value+'%'

            }"

        ></div>

    </div>

</div>

</template>

<script setup>

defineProps({

    title:String,

    label:String,

    value:Number

})

</script>

<style scoped>

.progress-card{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0 8px 24px rgba(0,0,0,.05);

}

.progress{

height:12px;

border-radius:12px;

overflow:hidden;

}

.progress-bar{

border-radius:12px;

}

h6{

font-weight:700;

color:#0F172A;

margin:0;

}

small{

color:#64748B;

}

</style>