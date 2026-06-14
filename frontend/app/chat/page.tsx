"use client";

import { useState } from "react";
import { askQuestion } from "@/lib/api";
import ReactMarkdown from "react-markdown";

interface Citation {
  document: string;
  page: number;
  image_path: string;
}

interface ChatAnswer {
  answer: string;
  citations?: Citation[];
}

export default function ChatPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState<ChatAnswer | null>(null);
  const [messages,setMessages] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const data = await askQuestion(question, messages);


setMessages(prev => [
  ...prev,
  {
    role:"user",
    content:question
  },
  {
    role:"assistant",
    content:data.answer
  }
]);


setAnswer(data);
setQuestion("");
    } catch (error) {
      console.error(error);

      setAnswer({
        answer: "Failed to get response from server.",
      });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="max-w-4xl mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">
        Chat with Documents
      </h1>

      {messages.map((msg, index) => (
        <div key={index} className="mb-3">
          <b>{msg.role === "user" ? "You:" : "AI:"}</b>

          <p>{msg.content}</p>
        </div>
      ))}

      <div className="flex gap-2">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask something..."
          className="flex-1 border rounded px-4 py-2"
        />

        <button
          onClick={handleAsk}
          disabled={loading}
          className="bg-black text-white px-4 py-2 rounded"
        >
          {loading ? "Thinking..." : "Ask"}
        </button>
      </div>

      {answer && (
        <div className="mt-8">
          <div className="border rounded-lg p-6 bg-white shadow-sm">
            <h2 className="font-bold text-lg mb-4">
              Answer
            </h2>

            <div className="prose max-w-none">
              <ReactMarkdown>
                {answer.answer}
              </ReactMarkdown>
            </div>
          </div>

          {answer.citations &&
            answer.citations.length > 0 && (
              <div className="mt-6">
                <h3 className="font-bold text-lg mb-3">
                  Sources
                </h3>

                <div className="space-y-3">
                  {answer.citations.map((citation, index) => (
                    <div
                      key={index}
                      className="border rounded-lg p-3 bg-gray-50"
                    >
                      <p>
                        📄 <strong>{citation.document}</strong>
                      </p>

                      <p>
                        📌 Page {citation.page}
                      </p>

                      <a
                       href={`http://127.0.0.1:8000/${citation.image_path.replace(/\\/g, "/")}`}
                       target="_blank"
                       rel="noopener noreferrer"
                      >
                      <img
                        src={`http://127.0.0.1:8000/${citation.image_path.replace(/\\/g, "/")}`}
                        alt="page preview"
                        className="mt-2 rounded border max-w-sm cursor-pointer"
                      />
                    </a>
                    </div>
                  ))}
                </div>
              </div>
            )}
        </div>
      )}
    </main>
  );
}