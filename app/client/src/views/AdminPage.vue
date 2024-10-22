<script setup>
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
//* ===== Shadcn =====
import { Icon } from '@iconify/vue'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'


const token = localStorage.getItem('token')

if (!token) {
  setTimeout(() => {
    router.push('/login')
  }, 2000)
}

const projectStructure = ref(
  {
    "_id": "66baecd6ed46e383b86a5484",
    "created_at": "",
    "description": "something",
    "github": "github.com/Alexsander33set/weather-forecast-project",
    "is_private": false,
    "name": "Weather Forecast",
    "slug": "weather-forecast",
    "status": "done",
    "technologies": [
      "java",
      "node",
      "python"
    ],
    "url": "apfs.com.br"
  })

const project = ref({
  name: "",
  slug: "",
  description: "",
  github: "",
  is_private: "",
  url: "",
  technologies: [],
  status: "",
  image: ""
})

const imageChanged = ref("#")
function changeImage(event){
  
  let smg = event.target.files
  imageChanged.value = (URL.createObjectURL(smg[0]))
  console.log(smg)
  console.log(imageChanged.value)
}



import { ComboboxAnchor, ComboboxContent, ComboboxInput, ComboboxPortal, ComboboxRoot } from 'radix-vue'
import { CommandEmpty, CommandGroup, CommandItem, CommandList } from '@/components/ui/command'
import { TagsInput, TagsInputInput, TagsInputItem, TagsInputItemDelete, TagsInputItemText } from '@/components/ui/tags-input'

const frameworks = [
  { value: 'vue', label: 'Vue 3' },
  { value: 'vite', label: 'Vite' },
  { value: 'nuxt', label: 'Nuxt' },
  { value: 'remix', label: 'Remix' },
  { value: 'astro', label: 'Astro' },
]

const modelValue = ref([])
const open = ref(false)
const searchTerm = ref('')

const filteredFrameworks = computed(() => frameworks.filter(i => !modelValue.value.includes(i.label)))
</script>

<template>
    <template v-if="!token">
      <Alert variant="destructive" class="m-4">
        <Icon icon="lucide:alert-circle" class="w-4 h-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Your session has expired. Please log in again.
        </AlertDescription>
      </Alert>
    </template>
    
    <template v-else>
      <h1>Admin Page</h1>
    </template>
  <main class="container flex-1">
      <hr>
    <h3>Input projects</h3>
    {{ projectStructure }}

    <section class="border p-4 flex flex-col gap-2">
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="name">Name</Label>
        <Input id="name" type="text" v-model="project.name" placeholder="name" />
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="slug">Slug</Label>
        <Input id="slug" type="text" v-model="project.slug" placeholder="slug" />
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="description">Description</Label>
        <Input id="description" type="text" v-model="project.description" placeholder="description" />
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="name">Technologies</Label>
        <TagsInput class="px-0 gap-0 w-100" :model-value="modelValue">
          <div class="flex gap-2 flex-wrap items-center px-3">
            <TagsInputItem v-for="item in modelValue" :key="item" :value="item">
              <TagsInputItemText />
              <TagsInputItemDelete />
            </TagsInputItem>
          </div>
      
          <ComboboxRoot v-model="modelValue" v-model:open="open" v-model:searchTerm="searchTerm" class="w-full">
            <ComboboxAnchor as-child>
              <ComboboxInput placeholder="Framework..." as-child>
                <TagsInputInput class="w-full px-3" :class="modelValue.length > 0 ? 'mt-2' : ''" @keydown.enter.prevent />
              </ComboboxInput>
            </ComboboxAnchor>
      
            <ComboboxPortal>
              <ComboboxContent>
                <CommandList
                  position="popper"
                  class="w-[--radix-popper-anchor-width] rounded-md mt-2 border bg-popover text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2"
                >
                  <CommandEmpty />
                  <CommandGroup>
                    <CommandItem
                      v-for="framework in filteredFrameworks" :key="framework.value" :value="framework.label"
                      @select.prevent="(ev) => {
                        if (typeof ev.detail.value === 'string') {
                          searchTerm = ''
                          modelValue.push(ev.detail.value)
                        }
      
                        if (filteredFrameworks.length === 0) {
                          open = false
                        }
                      }"
                    >
                      {{ framework.label }}
                    </CommandItem>
                  </CommandGroup>
                </CommandList>
              </ComboboxContent>
            </ComboboxPortal>
          </ComboboxRoot>
        </TagsInput>
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="url">URL</Label>
        <Input id="url" type="text" v-model="project.url" placeholder="https://www.google.com" />
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="status">Status</Label>
        <Input id="status" type="text" v-model="project.status" placeholder="status" />
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="name">Privacidade</Label>
        <Input type="text" v-model="project.is_private" placeholder="Privado?" /> Publico / Privado
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="created_at">Criado em</Label>
        <Input id="created_at" type="date" v-model="project.created_at" placeholder="dd/mm/aaaa" />
      </div>
      <div class="grid w-full max-w-sm items-center gap-1.5">
        <Label for="picture">Foto</Label>
        <Input id="picture" type="file" accept="image/*"
          v-model="project.image" 
          @change="changeImage"/>
        <template v-if="project.image">
        <div>
          <p>Preview</p>
          <img :src="imageChanged" alt="pho">
        </div>
        </template>
          
      </div>
    </section>
  </main>
</template>