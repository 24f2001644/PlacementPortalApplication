<script setup>

import { computed } from "vue"

const props = defineProps({

    title:String,

    value:[String,Number],

    color:String,

    icon:String,

    subtitle:String

})

const bgColor = computed(()=>{

    switch(props.color){

        case "primary":
            return "#EEF2FF"

        case "success":
            return "#ECFDF5"

        case "warning":
            return "#FEF3C7"

        case "danger":
            return "#FEE2E2"

        default:
            return "#F8FAFC"

    }

})

const iconColor = computed(()=>{

    switch(props.color){

        case "primary":
            return "#4F46E5"

        case "success":
            return "#22C55E"

        case "warning":
            return "#F59E0B"

        case "danger":
            return "#EF4444"

        default:
            return "#64748B"

    }

})

</script>

<template>

<div class="stats-card">

    <div
        class="icon-box"
        :style="{
            background:bgColor,
            color:iconColor
        }"
    >

        <i :class="icon"></i>

    </div>

    <div>

        <div class="title">

            {{ title }}

        </div>

        <div class="value">

            {{ value }}

        </div>

        <div class="subtitle">

            {{ subtitle }}

        </div>

    </div>

</div>

</template>

<style scoped>

.stats-card{

background:white;

padding:25px;

border-radius:18px;

display:flex;

gap:18px;

align-items:center;

box-shadow:0 15px 35px rgba(0,0,0,.08);

transition:.3s;

}

.stats-card:hover{

transform:translateY(-6px);

}

.icon-box{

width:65px;

height:65px;

border-radius:18px;

display:flex;

justify-content:center;

align-items:center;

font-size:28px;

}

.title{

font-size:14px;

color:#64748B;

}

.value{

font-size:34px;

font-weight:700;

color:#1E293B;

}

.subtitle{

font-size:13px;

color:#94A3B8;

}

</style>