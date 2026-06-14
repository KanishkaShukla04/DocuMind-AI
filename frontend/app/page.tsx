export default function HomePage() {
  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center">
      <h1 className="text-6xl font-bold mb-4">
        DocuMind AI
      </h1>

      <p className="text-gray-400 mb-10">
        AI-Powered Document Intelligence
      </p>

      <div className="flex gap-4">
        <a
          href="/upload"
          className="px-6 py-3 bg-blue-600 rounded-lg hover:bg-blue-700"
        >
          Upload Documents
        </a>

        <a
          href="/chat"
          className="px-6 py-3 bg-green-600 rounded-lg hover:bg-green-700"
        >
          Chat with Documents
        </a>
      </div>
    </main>
  );
}