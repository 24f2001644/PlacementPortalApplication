<script setup>
import { computed } from "vue"

const props = defineProps({

    label: String,

    type: {
        type: String,
        default: "secondary"
    }

})

const badgeClass = computed(() => {

    return `bg-${props.type}`

})
</script>

<template>

<span
    class="badge rounded-pill"
    :class="badgeClass"
>

    {{ label }}

</span>

</template>