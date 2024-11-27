import { ref } from 'vue'
import axios from 'axios'
import { defineStore } from 'pinia'

/**
 * Provides a Pinia store for managing project-related data.
 *
 * The `useProjectsStore` function defines a Pinia store with the following properties and methods:
 *
 * - `projects`: a reactive ref that holds an array of project objects.
 * - `projectsMockup`: an array of sample project objects used for fallback when the API request fails.
 * - `getProjects()`: an asynchronous function that fetches project data from an API and updates the `projects` ref.
 *
 * The store is registered with the name 'projects'.
 */
export const useProjectsStore = defineStore('projects', () => {
//* ========>> Projects  <<========

  const projects = ref([])
  const isFetchingProjects = ref(false)

  const projectsMockup = [
    {
      "_id": "66baecd6ed46e383b86a5484",
      "name": "projectsMockup",
      "slug": "projects-mockup",
      "description": "projectsMockup",
      "technologies": [
        "java",
        "node",
        "python"
      ],
      "url": "https://www.apfs.com.br",
      "is_private": false,
      "created_at": 1723526343.82374
    },
    {
      "_id": "66baf3812ffa799538467a33",
      "name": "Weather Forecast",
      "slug": "weather-forecast",
      "description": `This weather forecast application is a monolithic project developed using **Flask** for the backend and **Vue** with the **Vuetify** component framework for the frontend. The backend handles both API routes and frontend rendering, integrating the frontend build generated by **Vite** (\`vite build\`) into the project.

---

#### **Key Features:**

1. **Flask Backend:**
   - Serves the static files generated by Vue/Vuetify.
   - Provides API routes to fetch weather data from third-party services.
   - Manages business logic and external service integrations.

2. **Vue and Vuetify Frontend:**
   - A responsive and modern interface displaying information such as temperature, weather conditions, and forecasts.
   - Uses Vuetify’s custom components for tables, charts, and general data presentation.

3. **Monolithic Architecture:**
   - Combines backend and frontend into a single application, simplifying deployment and maintenance.

---`,
      "technologies": [
        "java",
        "node",
        "python"
      ],
      "url": "https://www.apfs.com.br",
      "is_private": false,
      "created_at": 1723528060
    },
    {
      "_id": "66baf3b55b1172f323a2cc99",
      "name": "Weather Forecast",
      "slug": "weather-forecast",
      "description": "something",
      "technologies": [
        "python",
        "flask",
        "vue",
        "vuetify"
      ],
      "url": "https://www.apfs.com.br",
      "is_private": false,
      "created_at": 1723528108
    }
  ]

  const getProjects = async () => {
    try {
      isFetchingProjects.value = true
      // to test at local env running server: http://localhost:80
      let response = await axios.get("/api/projects")
      let { data, headers, status } = response

      if (status == 200 && headers['content-type'] == "application/json") {
        projects.value = data
        isFetchingProjects.value = false
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

  getProjects()


  const deleteProject = (projectID) =>{
    console.log(`delete: ${projectID} called`)
    /**
    [x] Get project name
    [x] Send a double check
    [ ] Validade
    [x] call delete project api
  */
    axios.delete(`/api/delete-project/${projectID}`)
      .then(response => {response.status == 200 || console.log("Project deleted")})
      .catch(error => {console.log(error)})
  }

  return {
    projects, deleteProject, isFetchingProjects
  }
})
