import { useState } from "react"

/**
 * Main application component that handles the UI layout, 
 * theme toggling, and the overall image detection workflow.
 */
function App() {
  const [file, setFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [dragActive, setDragActive] = useState(false)
  const [darkMode, setDarkMode] = useState(true)

  /**
   * Processes a selected image file by saving it to state 
   * and generating a temporary URL to show a preview on the screen.
   */
  const handleFile = (selectedFile) => {
    setFile(selectedFile)
    setPreview(URL.createObjectURL(selectedFile))
    setResult(null)
  }

  /**
   * Manages the "Drop" event when a user drags a file over the upload area, 
   * extracting the file and passing it to the file handler.
   */
  const handleDrop = (e) => {
    e.preventDefault()
    setDragActive(false)

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0])
    }
  }

  /**
   * Sends the uploaded image to the FastAPI backend, handles the 
   * loading animation, and saves the AI's prediction result to the state.
   */
  const handleSubmit = async () => {
    if (!file) {
      alert("Please upload an image")
      return
    }

    setLoading(true)

    const formData = new FormData()
    formData.append("file", file)

    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        body: formData,
      })

      const data = await response.json()
      setResult(data)
    } catch (error) {
      alert("Error connecting to backend")
    }

    setLoading(false)
  }

  return (
    <div
      className={`min-h-screen flex items-center justify-center px-4 transition-all duration-500 ${
        darkMode
          ? "bg-gradient-to-br from-indigo-900 via-purple-900 to-cyan-900"
          : "bg-gradient-to-br from-pink-100 via-purple-100 to-blue-100"
      }`}
    >
      {/* Theme Toggle */}
      <button
        onClick={() => setDarkMode(!darkMode)}
        className={`absolute top-6 right-6 px-4 py-2 rounded-lg text-sm font-medium transition ${
          darkMode
            ? "bg-gray-800 text-gray-200 hover:bg-gray-700"
            : "bg-white text-gray-700 border hover:bg-gray-100"
        }`}
      >
        {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
      </button>

      {/* Card */}
      <div
        className={`rounded-3xl p-8 w-full max-w-lg shadow-2xl backdrop-blur-xl border transition-all ${
          darkMode
            ? "bg-black/40 border-purple-700"
            : "bg-white/80 border-purple-200"
        }`}
      >
        {/* Title */}
        <h1
          className={`text-3xl font-bold text-center ${
            darkMode ? "text-white" : "text-gray-900"
          }`}
        >
          AI Image Detector
        </h1>

        <p
          className={`text-center mt-2 mb-6 ${
            darkMode ? "text-purple-200" : "text-gray-500"
          }`}
        >
          Analyze images for AI-generated content
        </p>

        {/* Upload Area */}
        <div
          onDragOver={(e) => {
            e.preventDefault()
            setDragActive(true)
          }}
          onDragLeave={() => setDragActive(false)}
          onDrop={handleDrop}
          className={`border-2 border-dashed rounded-2xl p-6 text-center transition-all ${
            dragActive
              ? "border-cyan-400 bg-cyan-400/10"
              : darkMode
              ? "border-purple-600 bg-purple-900/20 hover:border-cyan-400"
              : "border-purple-300 bg-white hover:border-blue-400"
          }`}
        >
          <input
            type="file"
            accept="image/*"
            className="hidden"
            id="fileUpload"
            onChange={(e) => handleFile(e.target.files[0])}
          />

          <label htmlFor="fileUpload" className="cursor-pointer">
            <p className={darkMode ? "text-purple-200" : "text-gray-600"}>
              Drag & Drop or{" "}
              <span className="text-cyan-400 font-semibold">
                Browse Files
              </span>
            </p>
          </label>
        </div>

        {/* Preview */}
        {preview && (
          <img
            src={preview}
            alt="preview"
            className="mt-6 rounded-xl border max-h-72 mx-auto shadow-xl"
          />
        )}

        {/* Analyze Button */}
        <button
          onClick={handleSubmit}
          disabled={loading}
          className="mt-6 w-full bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 hover:from-cyan-300 hover:to-purple-400 text-white font-semibold py-3 rounded-xl transition flex items-center justify-center gap-2 disabled:opacity-60"
        >
          {loading && (
            <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
          )}

          {loading ? "Analyzing..." : "Analyze Image"}
        </button>

        {/* Result */}
        {result && !loading && (
          <div
            className={`mt-8 p-6 rounded-2xl border ${
              darkMode
                ? "bg-black/40 border-purple-700"
                : "bg-white border-purple-200"
            }`}
          >
            <h2
              className={`text-xl font-semibold text-center ${
                result.label === "AI-generated"
                  ? "text-red-400"
                  : "text-green-400"
              }`}
            >
              {result.label}
            </h2>

            <p
              className={`text-center text-sm mt-2 ${
                darkMode ? "text-purple-200" : "text-gray-500"
              }`}
            >
              AI-generated likelihood: {(result.score * 100).toFixed(2)}%
            </p>

            {/* Probability Bar */}
            <div className="w-full bg-gray-300 dark:bg-gray-700 rounded-full h-3 mt-4 overflow-hidden">
              <div
                className={`h-3 rounded-full transition-all duration-1000 ${
                  result.label === "AI-generated"
                    ? "bg-red-500"
                    : "bg-green-500"
                }`}
                style={{ width: `${result.score * 100}%` }}
              ></div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App