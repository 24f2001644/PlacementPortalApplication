<script setup>

const props = defineProps({

    title: String,

    value: Number,

    total: Number,

    color: String

})

const percentage = computed(() => {

    if (!props.total) return 0

    return Math.round((props.value / props.total) * 100)

})

import { computed } from "vue"

</script>

<template>

<div class="card admin-card shadow-sm h-100">

    <div class="card-body">

        <div class="d-flex justify-content-between">

            <h6>{{ title }}</h6>

            <strong>{{ percentage }}%</strong>

        </div>

        <div class="progress mt-3">

            <div

                class="progress-bar"

                :class="'bg-'+color"

                :style="{

                    width: percentage+'%'

                }"

            >

            </div>

        </div>

        <div class="mt-3">

            {{ value }}

            /

            {{ total }}

        </div>

    </div>

</div>

</template>