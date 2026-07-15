<script setup>

const props = defineProps({

    text: String,

    icon: String,

    color: {
        type: String,
        default: "primary"
    },

    disabled: {
        type: Boolean,
        default: false
    }

})

const emit = defineEmits(["click"])

</script>

<template>

<button

    class="btn"

    :class="'btn-' + color"

    :disabled="disabled"

    @click="emit('click')"

>

    <i
        v-if="icon"
        :class="icon"
        class="me-2"
    ></i>

    {{ text }}

</button>

</template>