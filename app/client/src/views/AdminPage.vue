<script setup>
import { ref, computed, watch } from 'vue'
import axios from 'axios'

//* ===== Shadcn =====
import { Icon } from '@iconify/vue'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'
import { Label } from '@/components/ui/label'
import { Switch } from '@/components/ui/switch'

import {
  Table,
  TableBody,
  // TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import { Select,SelectContent,SelectGroup,SelectItem,/*SelectLabel,*/SelectTrigger,SelectValue } from '@/components/ui/select'
import { ComboboxAnchor, ComboboxContent, ComboboxInput, ComboboxPortal, ComboboxRoot } from 'radix-vue'
import { CommandEmpty, CommandGroup, CommandItem, CommandList } from '@/components/ui/command'
import { TagsInput, TagsInputInput, TagsInputItem, TagsInputItemDelete, TagsInputItemText } from '@/components/ui/tags-input'


//* =============== Projects ===============

const projects = ref([
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
  },
  {
    "_id": "66baecd6ed46e383b86a5484",
    "created_at": "",
    "description": "something",
    "github": "github.com/Alexsander33set/weather-forecast-project",
    "is_private": false,
    "name": "Weather Forecast",
    "slug": "weather-forecast",
    "status ": "done"
  }
])

const projectsMockup = [
    {
        "_id": "66baecd6ed46e383b86a5484",
        "name": "Weather Forecast",
        "slug": "weather-forecast",
        "description": "something",
        "technologies": [
            "java",
            "node",
            "python"
        ],
        "url": "www.apfs.com.br",
        "is_private": false,
        "created_at": 1723526343.82374
    },
    {
        "_id": "66baf3812ffa799538467a33",
        "name": "Weather Forecast",
        "slug": "weather-forecast",
        "description": "something",
        "technologies": [
            "java",
            "node",
            "python"
        ],
        "url": "www.apfs.com.br",
        "is_private": false,
        "created_at": 1723528060
    },
    {
        "_id": "66baf3b55b1172f323a2cc99",
        "name": "Weather Forecast",
        "slug": "weather-forecast",
        "description": "something",
        "technologies": [
            "java",
            "node",
            "python"
        ],
        "url": "www.apfs.com.br",
        "is_private": false,
        "created_at": 1723528108
    }
]

async function getProjects(){
  try{
    // to test at local env running server: http://localhost:80
    let response = await axios.get("/api/projects")
    let {data, headers, status} = response

    if (status == 200 || headers['content-type'] == "application/json"){
      projects.value = data
    } else {
      console.warn(">> Invalid Request <<")
      projects.value = null
    }
  } catch (err) {
    console.error(err)
    // projects.value = null
    projects.value = projectsMockup
  }
}

//* =============== Projects Operations ===============

function editProject(projectName) {
  console.log("edit: " + projectName)
/**
  [x] Get project name
  [ ] Select the project from the list
  [ ] Populate the form
  [ ] Open  the form
*/
}

function deleteProject(projectName){
  console.log("delete: " +  projectName)
  /**
  [x] Get project name
  [ ] Send a double check
  [ ] Validade
  [ ] call delete project api
*/
  // axios.delete("http://localhost:80/api/delete-project/",{data: {name: projectName}}) 
}


//* =============== Form ===============

const form = ref({
  data: {},
  isOpen: false,
  process: ""
})

const imageChanged = ref("#")
function changeImage(event) {

  let smg = event.target.files
  imageChanged.value = (URL.createObjectURL(smg[0]))
  console.log(smg)
  console.log(imageChanged.value)
}

const frameworks = [
  { value: 'vue', label: 'Vue 3' },
  { value: 'vite', label: 'Vite' },
  { value: 'nuxt', label: 'Nuxt' },
  { value: 'remix', label: 'Remix' },
  { value: 'astro', label: 'Astro' },
]
const statusList = [
  { value: 'planning', label: 'Planning' },  
  { value: 'todo', label: 'To do' },
  { value: 'doing', label: 'Doing' },
  { value: 'done', label: 'Done' }
]

const modelValue = ref([])
const open = ref(false)
const searchTerm = ref('')

const filteredFrameworks = computed(() => frameworks.filter(i => !modelValue.value.includes(i.label)))


getProjects()


</script>

<template>
  <main class="container flex-1">
    <header class="mt-8">
      <h2 class="text-5xl font-thin">Adminstration Page</h2>
      <hr>
    </header>
    <section v-if="!form.isOpen" class="flex flex-col mt-8 gap-2">
      <h3 class="text-4xl">Projects</h3>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead class="text-nowrap max-w-60">
              Application Name
            </TableHead>
            <TableHead>Status</TableHead>
            <TableHead>GitHub</TableHead>
            <TableHead>URL</TableHead>
            <TableHead class="text-center">Edit</TableHead>
            <TableHead class="text-center">Delete</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(project, i) in projects" :key="i">
            <TableCell class="font-medium">
              {{ project.name }}
            </TableCell>
            <TableCell>{{ project.status }}</TableCell>
            <TableCell>
              <template v-if="project.github">
              <a :href="project.github" class="hover:text-blue-500 transition-colors">
                {{ (project.github.split('/')[project.github.split('/').length - 1]) }}
              </a>
              </template>
              <template v-else><p class="text-gray-600">None</p></template>
              
            </TableCell>
            <TableCell>
              <a v-if="project.url" :href="project.url" class="hover:text-blue-500 transition-colors">{{ project.url
                }}</a>
              <p v-else class="text-gray-600">None</p>
            </TableCell>
            <TableCell class="text-center">
              <Button @click="editProject(project.slug)" variant="outline">
                <Icon icon="mdi:edit-outline" class="-m-1 scale-125" />
              </Button>
            </TableCell>
            <TableCell class="text-center">
              <Button @click="deleteProject(project.slug)" variant="outline">
                <Icon icon="mdi:delete-outline" class="-m-1 scale-125 text-red-600 dark:text-red-400" />
              </Button>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
      <div class="h-10">
        <span class="float-right">
          <Button @click="form.isOpen = true" class="flex gap-2 items-center p-2">
            <Icon icon="mdi:plus-circle-outline" /> Add Project
          </Button>
        </span>
      </div>
    </section>


    <form v-if="form.isOpen" class="my-10">
      <h3 class="text-3xl">Change App</h3>
      <section class="border p-4 mt-4 flex flex-col gap-2 rounded-md">
        <div class="flex items-center gap-1.5">
          <Label for="name">Name:</Label>
          <Input id="name" type="text" v-model="project.name" placeholder="Project Name" />
          <Select>
            <SelectTrigger class="w-[180px]">
              <SelectValue placeholder="Status" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem v-for="(status, index) in statusList" :key="index" :value="status.value">
                  {{ status.label }}
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <section class="border rounded-sm my-1 p-4 py-2 transition-all delay-150 duration-500 flex flex-col gap-2">
            <div class="flex gap-2 items-center">
              <h5>Is Private?</h5>
              <Switch v-model="form.data.is_private" @click="form.data.is_private = !form.data.is_private" />
            </div>
            <section v-if="!form.data.is_private" class="flex flex-col gap-2 mt-2">
              <div>
                <Label for="url">URL</Label>
                <Input id="url" type="text" v-model="form.data.url" placeholder="https://url.com" />
              </div>
              <div>
                <Label for="github">GitHub</Label>
                <Input id="github" type="text" v-model="form.data.github"
                  placeholder="https://github.com/Alexsander33set/..." />
              </div>
            </section>
        </section>
        <div class="grid items-center gap-1.5">
          <Label for="description">Description</Label>
          <Textarea id="description" v-model="project.description" placeholder="Project Description" />
        </div>
        <div class="grid items-center gap-1.5">
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
                <ComboboxInput placeholder="Programming Language, Library, Framework..." as-child>
                  <TagsInputInput class="w-full px-3" :class="modelValue.length > 0 ? 'mt-2' : ''"
                    @keydown.enter.prevent />
                </ComboboxInput>
              </ComboboxAnchor>

              <ComboboxPortal>
                <ComboboxContent>
                  <CommandList position="popper"
                    class="w-[--radix-popper-anchor-width] rounded-md mt-2 border bg-popover text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2">
                    <CommandEmpty />
                    <CommandGroup>
                      <CommandItem v-for="framework in filteredFrameworks" :key="framework.value"
                        :value="framework.label" @select.prevent="(ev) => {
                          if (typeof ev.detail.value === 'string') {
                            searchTerm = ''
                            modelValue.push(ev.detail.value)
                          }

                          if (filteredFrameworks.length === 0) {
                            open = false
                          }
                        }">
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
          <Label for="status">Status</Label>
          <Input id="status" type="text" v-model="project.status" placeholder="status" />
        </div>
        <div class="grid w-full max-w-sm items-center gap-1.5">
          <Label for="created_at">Iniciado em</Label>
          <Input id="created_at" type="date" v-model="project.created_at" placeholder="dd/mm/aaaa" />
        </div>
        <div class="grid w-full max-w-sm items-center gap-1.5">
          <Label for="picture">Foto</Label>
          <Input id="picture" type="file" accept="image/*" @change="changeImage" />
          <template v-if="project.image">
            <div>
              <p>Preview</p>
              <img :src="imageChanged" alt="pho">
            </div>
          </template>
        </div>
      </section>
      <section class="mt-2 flex justify-end gap-4">
        <Button class="float-right">Cancel</Button>
        <Button class="float-right" type="submit">Save</Button>
      </section>
    </form>
  </main>
</template>