// import { useState } from "react";

// export default function FileUpload() {
//   const [selectedFile, setSelectedFile] = useState(null);
//   const [uploadStatus, setUploadStatus] = useState("");

//   const handleFileChange = (e) => {
//     setSelectedFile(e.target.files[0]);
//   };

//   const handleDrop = (e) => {
//     e.preventDefault();
//     setSelectedFile(e.dataTransfer.files[0]);
//   };

//   const handleDragOver = (e) => {
//     e.preventDefault();
//   };

//   const handleUpload = () => {
//     if (!selectedFile) return;

//     const formData = new FormData();
//     formData.append("file", selectedFile);

//     setUploadStatus("Uploading...");

//     fetch("http://localhost:8000/upload", {
//       method: "POST",
//       body: formData,
//     })
//       .then((res) => res.json())
//       .then((data) => {
//         setUploadStatus(`✅ ${data.message}`);
//       })
//       .catch((err) => {
//         console.error(err);
//         setUploadStatus("❌ Upload failed");
//       });
//   };

//   return (
//     <div className="flex h-screen bg-gray-100 overflow-hidden">
//       {/* Sidebar */}
//       <aside className="w-64 bg-white shadow-md border-r flex flex-col p-6 space-y-6">
//         <h2 className="text-xl font-bold text-gray-800">Upload Panel</h2>

//         <div
//           onDrop={handleDrop}
//           onDragOver={handleDragOver}
//           className="border-2 border-dashed border-gray-400 rounded-lg p-4 text-center"
//         >
//           {selectedFile ? (
//             <p className="text-green-600 font-medium text-sm">{selectedFile.name}</p>
//           ) : (
//             <p className="text-gray-500 text-sm">Drag & drop your meeting file here</p>
//           )}
//           <input
//             type="file"
//             accept=".mp3,.mp4,.wav,.m4a"
//             onChange={handleFileChange}
//             className="hidden"
//             id="fileInput"
//           />
//           <label
//             htmlFor="fileInput"
//             className="mt-2 inline-block bg-blue-600 text-white px-4 py-2 rounded text-sm cursor-pointer hover:bg-blue-700 transition"
//           >
//             Or Choose File
//           </label>
//         </div>

//         <button
//           onClick={handleUpload}
//           disabled={!selectedFile}
//           className="bg-green-600 text-white py-2 rounded hover:bg-green-700 transition disabled:bg-gray-300 disabled:cursor-not-allowed"
//         >
//           Upload & Process
//         </button>
//       </aside>

//       {/* Main Content */}
//       <main className="flex-1 overflow-auto p-10">
//         <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">
//           🎙️ AI Meeting Insight Dashboard
//         </h1>

//         {uploadStatus && (
//           <div className="mt-10 text-center text-lg text-gray-700">
//             {uploadStatus}
//           </div>
//         )}
//       </main>
//     </div>
//   );
// }


import { useState } from "react";

export default function FileUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [transcript, setTranscript] = useState("");
  const [insights, setInsights] = useState("");

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setSelectedFile(e.dataTransfer.files[0]);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    setUploadStatus("Uploading...");
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const uploadRes = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });
      const uploadData = await uploadRes.json();
      setUploadStatus(`✅ ${uploadData.message}`);

      const filename = selectedFile.name;
      setUploadStatus("Transcribing...");

      const transcribeRes = await fetch(`http://localhost:8000/transcribe/${filename}`);
      const transcribeData = await transcribeRes.json();

      if (transcribeData.transcript) {
        setTranscript(transcribeData.transcript);
        setUploadStatus("Extracting insights...");

        const insightRes = await fetch("http://localhost:8000/extract_insights", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ transcript: transcribeData.transcript }),
        });

        const insightData = await insightRes.json();
        if (insightData.insights) {
          setInsights(insightData.insights);
          setUploadStatus("✅ Done! Insights generated below.");
        } else {
          setUploadStatus("❌ Failed to generate insights");
        }
      } else {
        setUploadStatus("❌ Transcription failed");
      }
    } catch (err) {
      console.error(err);
      setUploadStatus("❌ Something went wrong");
    }
  };

  return (
    <div className="flex h-screen bg-gray-100 overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 bg-white shadow-md border-r flex flex-col p-6 space-y-6">
        <h2 className="text-xl font-bold text-gray-800">Upload Panel</h2>

        <div
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          className="border-2 border-dashed border-gray-400 rounded-lg p-4 text-center"
        >
          {selectedFile ? (
            <p className="text-green-600 font-medium text-sm">{selectedFile.name}</p>
          ) : (
            <p className="text-gray-500 text-sm">Drag & drop your meeting file here</p>
          )}
          <input
            type="file"
            accept=".mp3,.mp4,.wav,.m4a"
            onChange={handleFileChange}
            className="hidden"
            id="fileInput"
          />
          <label
            htmlFor="fileInput"
            className="mt-2 inline-block bg-blue-600 text-white px-4 py-2 rounded text-sm cursor-pointer hover:bg-blue-700 transition"
          >
            Or Choose File
          </label>
        </div>

        <button
          onClick={handleUpload}
          disabled={!selectedFile}
          className="bg-green-600 text-white py-2 rounded hover:bg-green-700 transition disabled:bg-gray-300 disabled:cursor-not-allowed"
        >
          Upload & Extract Insights
        </button>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto p-10">
        <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">
          🎙️ AI Meeting Insight Dashboard
        </h1>

        {uploadStatus && (
          <div className="mt-4 text-center text-lg text-gray-700">
            {uploadStatus}
          </div>
        )} 

        {transcript && (
          <div className="mt-10">
            <h2 className="text-2xl font-bold mb-2 text-gray-800">📝 Transcript</h2>
            <div className="bg-white p-4 rounded shadow text-sm whitespace-pre-wrap max-h-80 overflow-y-auto border border-gray-200">
              {transcript}
            </div>
          </div>
        )}

        {insights && (
          <div className="mt-10">
            <h2 className="text-2xl font-bold mb-2 text-gray-800">🔍 Extracted Insights</h2>
            <div className="bg-white p-4 rounded shadow text-sm whitespace-pre-wrap border border-gray-200">
              {insights}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
