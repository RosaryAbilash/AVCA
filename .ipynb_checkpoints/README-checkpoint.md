# AVCA

Step0:
source AvcaEnv/bin/activate

step 1:
 
 vllm serve Qwen/Qwen2.5-14B-Instruct     --port 8000     --dtype bfloat16     --max-model-len 8192     --gpu-memory-utilization 0.3


 step: 2

 streamlit run app.py \
    --server.port 8501 \
    --server.headless true \
    --server.enableCORS false \
    --server.enableXsrfProtection false