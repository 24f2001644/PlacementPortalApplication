<script setup>

defineProps({

label:String,

icon:String,

variant:String

})

const emit=defineEmits(["click"])

</script>

<template>

<button

class="btn"

:class="'btn-'+variant"

@click="emit('click')"

>

<i

:class="icon"

class="me-2"

></i>

{{ label }}

</button>

</template>