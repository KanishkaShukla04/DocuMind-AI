"use client";

import { useState } from "react";
import { uploadFile } from "@/lib/api";

export default function UploadPage() {
  const [files, setFiles] = useState<File[]>([]);
  const [result, setResult] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleUpload() {
    if (!files.length) return;

    setLoading(true);
    const data = await uploadFile(files);
    setResult((prev) => [...prev, ...data]);
    setLoading(false);
  }

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold">Upload Document</h1>

      <input
        type="file"
        multiple
        className="mt-4"
        onChange={(e) => setFiles(Array.from(e.target.files || []))}
      />

      <button
        onClick={handleUpload}
        className="ml-4 px-4 py-2 bg-black text-white rounded"
      >
        {loading ? "Uploading..." : "Upload"}
      </button>

      {result && (
        <div className="mt-6 border p-4 rounded">
          {result.map((doc: any) => (
            <div key={doc.document_id} className="mb-4">
              <p>📄 {doc.filename}</p>
              <p>Status: {doc.status}</p>
              <p>Document ID: {doc.document_id}</p>
              <p>Pages: {doc.pages}</p>
              {doc.classification && (
                <div className="mt-4">
                  <h3 className="font-bold">Classification</h3>
                  <p>Type: {doc.classification.document_type}</p>
                  <p>Topic: {doc.classification.topic}</p>
                  <p>Sensitivity: {doc.classification.sensitivity_level}</p>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}