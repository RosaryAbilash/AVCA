🚀 Initializing FINETUNE_001 Pipeline...
📦 Loading Model: Qwen/Qwen2.5-14B-Instruct
Generating train split: 5000 examples [00:00, 229312.22 examples/s]
Map: 100%|████████████████████████████████████████████████████████████████████████████████| 5000/5000 [00:00<00:00, 32177.99 examples/s]
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████| 663/663 [00:00<00:00, 2.03MB/s]
tokenizer_config.json: 100%|███████████████████████████████████████████████████████████████████████| 7.30k/7.30k [00:00<00:00, 8.59MB/s]
vocab.json: 100%|██████████████████████████████████████████████████████████████████████████████████| 2.78M/2.78M [00:00<00:00, 23.7MB/s]
merges.txt: 100%|██████████████████████████████████████████████████████████████████████████████████| 1.67M/1.67M [00:00<00:00, 45.5MB/s]
tokenizer.json: 100%|██████████████████████████████████████████████████████████████████████████████| 7.03M/7.03M [00:00<00:00, 83.8MB/s]
model.safetensors.index.json: 100%|████████████████████████████████████████████████████████████████| 47.5k/47.5k [00:00<00:00, 47.4MB/s]
Fetching 8 files: 100%|███████████████████████████████████████████████████████████████████████████████████| 8/8 [00:25<00:00,  3.21s/it]
Download complete: 100%|███████████████████████████████████████████████████████████████████████████| 29.5G/29.5G [00:29<00:00, 1.02GB/s]
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████| 579/579 [00:19<00:00, 29.06it/s]
generation_config.json: 100%|██████████████████████████████████████████████████████████████████████████| 242/242 [00:00<00:00, 1.23MB/s]
trainable params: 25,165,824 || all params: 14,795,199,488 || trainable%: 0.1701
Adding EOS to train dataset: 100%|████████████████████████████████████████████████████████| 5000/5000 [00:00<00:00, 16677.06 examples/s]
Tokenizing train dataset: 100%|████████████████████████████████████████████████████████████| 5000/5000 [00:02<00:00, 2485.15 examples/s]
🔥 Starting LoRA Fine-Tuning...
[transformers] The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values. Updated tokens: {'bos_token_id': None, 'pad_token_id': 151645}.
  0%|                                                                                                          | 0/1250 [00:00<?, ?it/s]/workspace/shared/avca-copilot/AvcaEnv/lib/python3.12/site-packages/transformers/models/qwen2/modeling_qwen2.py:108: UserWarning: Failed validator: ROCBLAS_VERSION (Triggered internally at /pytorch/aten/src/ATen/hip/tunable/Tunable.cpp:349.)
  freqs = (inv_freq_expanded.float() @ position_ids_expanded.float()).transpose(1, 2)
{'loss': '1.808', 'grad_norm': '0.9693', 'learning_rate': '3.6e-06', 'entropy': '0.7932', 'num_tokens': '1.489e+04', 'mean_token_accuracy': '0.6971', 'epoch': '0.016'}
{'loss': '1.771', 'grad_norm': '0.8725', 'learning_rate': '7.6e-06', 'entropy': '0.8009', 'num_tokens': '2.987e+04', 'mean_token_accuracy': '0.6978', 'epoch': '0.032'}
{'loss': '1.651', 'grad_norm': '0.6749', 'learning_rate': '1.16e-05', 'entropy': '0.8055', 'num_tokens': '4.47e+04', 'mean_token_accuracy': '0.7071', 'epoch': '0.048'}
{'loss': '1.488', 'grad_norm': '0.8559', 'learning_rate': '1.56e-05', 'entropy': '0.8006', 'num_tokens': '5.977e+04', 'mean_token_accuracy': '0.7208', 'epoch': '0.064'}      
{'loss': '1.215', 'grad_norm': '0.964', 'learning_rate': '1.96e-05', 'entropy': '0.8307', 'num_tokens': '7.458e+04', 'mean_token_accuracy': '0.7363', 'epoch': '0.08'}        
{'loss': '0.951', 'grad_norm': '0.8258', 'learning_rate': '2e-05', 'entropy': '0.875', 'num_tokens': '8.931e+04', 'mean_token_accuracy': '0.7737', 'epoch': '0.096'}          
{'loss': '0.6623', 'grad_norm': '0.6972', 'learning_rate': '1.999e-05', 'entropy': '0.7191', 'num_tokens': '1.043e+05', 'mean_token_accuracy': '0.8386', 'epoch': '0.112'}    
{'loss': '0.5052', 'grad_norm': '0.5671', 'learning_rate': '1.997e-05', 'entropy': '0.5283', 'num_tokens': '1.186e+05', 'mean_token_accuracy': '0.8785', 'epoch': '0.128'}    
{'loss': '0.4055', 'grad_norm': '0.3361', 'learning_rate': '1.995e-05', 'entropy': '0.4006', 'num_tokens': '1.334e+05', 'mean_token_accuracy': '0.8964', 'epoch': '0.144'}    
{'loss': '0.3829', 'grad_norm': '0.2547', 'learning_rate': '1.992e-05', 'entropy': '0.3698', 'num_tokens': '1.485e+05', 'mean_token_accuracy': '0.9033', 'epoch': '0.16'}     
{'loss': '0.3293', 'grad_norm': '0.3942', 'learning_rate': '1.988e-05', 'entropy': '0.3259', 'num_tokens': '1.634e+05', 'mean_token_accuracy': '0.9116', 'epoch': '0.176'}    
{'loss': '0.2721', 'grad_norm': '0.4019', 'learning_rate': '1.984e-05', 'entropy': '0.2561', 'num_tokens': '1.779e+05', 'mean_token_accuracy': '0.9275', 'epoch': '0.192'}    
{'loss': '0.2275', 'grad_norm': '0.8416', 'learning_rate': '1.979e-05', 'entropy': '0.2302', 'num_tokens': '1.925e+05', 'mean_token_accuracy': '0.9366', 'epoch': '0.208'}    
{'loss': '0.1888', 'grad_norm': '0.5342', 'learning_rate': '1.973e-05', 'entropy': '0.2052', 'num_tokens': '2.074e+05', 'mean_token_accuracy': '0.9462', 'epoch': '0.224'}    
{'loss': '0.1398', 'grad_norm': '0.6558', 'learning_rate': '1.967e-05', 'entropy': '0.1614', 'num_tokens': '2.222e+05', 'mean_token_accuracy': '0.9603', 'epoch': '0.24'}     
{'loss': '0.1252', 'grad_norm': '1.051', 'learning_rate': '1.96e-05', 'entropy': '0.147', 'num_tokens': '2.372e+05', 'mean_token_accuracy': '0.9643', 'epoch': '0.256'}       
{'loss': '0.08375', 'grad_norm': '0.6069', 'learning_rate': '1.952e-05', 'entropy': '0.1121', 'num_tokens': '2.518e+05', 'mean_token_accuracy': '0.9786', 'epoch': '0.272'}   
{'loss': '0.05325', 'grad_norm': '1.373', 'learning_rate': '1.944e-05', 'entropy': '0.08118', 'num_tokens': '2.67e+05', 'mean_token_accuracy': '0.9872', 'epoch': '0.288'}    
{'loss': '0.04104', 'grad_norm': '0.6528', 'learning_rate': '1.935e-05', 'entropy': '0.06192', 'num_tokens': '2.817e+05', 'mean_token_accuracy': '0.9899', 'epoch': '0.304'}  
{'loss': '0.02892', 'grad_norm': '0.4461', 'learning_rate': '1.925e-05', 'entropy': '0.04384', 'num_tokens': '2.961e+05', 'mean_token_accuracy': '0.9922', 'epoch': '0.32'}   
{'loss': '0.02947', 'grad_norm': '0.3217', 'learning_rate': '1.915e-05', 'entropy': '0.04165', 'num_tokens': '3.101e+05', 'mean_token_accuracy': '0.9921', 'epoch': '0.336'}  
{'loss': '0.02626', 'grad_norm': '0.3799', 'learning_rate': '1.904e-05', 'entropy': '0.03441', 'num_tokens': '3.251e+05', 'mean_token_accuracy': '0.9929', 'epoch': '0.352'}  
{'loss': '0.02591', 'grad_norm': '0.6662', 'learning_rate': '1.892e-05', 'entropy': '0.0356', 'num_tokens': '3.394e+05', 'mean_token_accuracy': '0.9927', 'epoch': '0.368'}   
{'loss': '0.02339', 'grad_norm': '0.4929', 'learning_rate': '1.88e-05', 'entropy': '0.02855', 'num_tokens': '3.543e+05', 'mean_token_accuracy': '0.9934', 'epoch': '0.384'}   
{'loss': '0.02305', 'grad_norm': '0.1569', 'learning_rate': '1.867e-05', 'entropy': '0.03111', 'num_tokens': '3.688e+05', 'mean_token_accuracy': '0.9934', 'epoch': '0.4'}    
{'loss': '0.02159', 'grad_norm': '0.2829', 'learning_rate': '1.854e-05', 'entropy': '0.02673', 'num_tokens': '3.838e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.416'}  
{'loss': '0.02293', 'grad_norm': '0.2877', 'learning_rate': '1.84e-05', 'entropy': '0.02935', 'num_tokens': '3.988e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.432'}    
{'loss': '0.02206', 'grad_norm': '0.4176', 'learning_rate': '1.826e-05', 'entropy': '0.02624', 'num_tokens': '4.134e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.448'}  
{'loss': '0.02168', 'grad_norm': '0.2395', 'learning_rate': '1.811e-05', 'entropy': '0.02608', 'num_tokens': '4.288e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.464'}   
{'loss': '0.02129', 'grad_norm': '0.2514', 'learning_rate': '1.795e-05', 'entropy': '0.02709', 'num_tokens': '4.44e+05', 'mean_token_accuracy': '0.9933', 'epoch': '0.48'}    
{'loss': '0.02007', 'grad_norm': '0.258', 'learning_rate': '1.779e-05', 'entropy': '0.02295', 'num_tokens': '4.587e+05', 'mean_token_accuracy': '0.994', 'epoch': '0.496'}    
{'loss': '0.02287', 'grad_norm': '0.3909', 'learning_rate': '1.762e-05', 'entropy': '0.02635', 'num_tokens': '4.732e+05', 'mean_token_accuracy': '0.9929', 'epoch': '0.512'}  
{'loss': '0.02058', 'grad_norm': '0.1566', 'learning_rate': '1.745e-05', 'entropy': '0.02542', 'num_tokens': '4.885e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.528'}   
{'loss': '0.02057', 'grad_norm': '0.1831', 'learning_rate': '1.727e-05', 'entropy': '0.02517', 'num_tokens': '5.032e+05', 'mean_token_accuracy': '0.9928', 'epoch': '0.544'}  
{'loss': '0.01957', 'grad_norm': '0.2452', 'learning_rate': '1.709e-05', 'entropy': '0.02287', 'num_tokens': '5.182e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.56'}   
{'loss': '0.02065', 'grad_norm': '0.1433', 'learning_rate': '1.69e-05', 'entropy': '0.02422', 'num_tokens': '5.329e+05', 'mean_token_accuracy': '0.9933', 'epoch': '0.576'}   
{'loss': '0.02171', 'grad_norm': '0.2663', 'learning_rate': '1.671e-05', 'entropy': '0.02456', 'num_tokens': '5.474e+05', 'mean_token_accuracy': '0.9925', 'epoch': '0.592'}  
{'loss': '0.02047', 'grad_norm': '0.3068', 'learning_rate': '1.651e-05', 'entropy': '0.02158', 'num_tokens': '5.626e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.608'}  
{'loss': '0.02159', 'grad_norm': '0.2054', 'learning_rate': '1.631e-05', 'entropy': '0.02582', 'num_tokens': '5.769e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.624'}   
{'loss': '0.02042', 'grad_norm': '0.2311', 'learning_rate': '1.611e-05', 'entropy': '0.02434', 'num_tokens': '5.916e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.64'}    
{'loss': '0.02107', 'grad_norm': '0.2707', 'learning_rate': '1.59e-05', 'entropy': '0.02322', 'num_tokens': '6.062e+05', 'mean_token_accuracy': '0.9932', 'epoch': '0.656'}   
{'loss': '0.01989', 'grad_norm': '0.2326', 'learning_rate': '1.569e-05', 'entropy': '0.02246', 'num_tokens': '6.208e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.672'}  
{'loss': '0.01919', 'grad_norm': '0.2651', 'learning_rate': '1.547e-05', 'entropy': '0.02121', 'num_tokens': '6.364e+05', 'mean_token_accuracy': '0.9932', 'epoch': '0.688'}  
{'loss': '0.02145', 'grad_norm': '0.1585', 'learning_rate': '1.525e-05', 'entropy': '0.02321', 'num_tokens': '6.503e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.704'}  
{'loss': '0.01823', 'grad_norm': '0.1366', 'learning_rate': '1.502e-05', 'entropy': '0.02258', 'num_tokens': '6.655e+05', 'mean_token_accuracy': '0.9941', 'epoch': '0.72'}   
{'loss': '0.02124', 'grad_norm': '0.1948', 'learning_rate': '1.479e-05', 'entropy': '0.02333', 'num_tokens': '6.801e+05', 'mean_token_accuracy': '0.9929', 'epoch': '0.736'}  
{'loss': '0.01946', 'grad_norm': '0.1781', 'learning_rate': '1.456e-05', 'entropy': '0.02164', 'num_tokens': '6.946e+05', 'mean_token_accuracy': '0.9939', 'epoch': '0.752'}  
{'loss': '0.02157', 'grad_norm': '0.2754', 'learning_rate': '1.433e-05', 'entropy': '0.02332', 'num_tokens': '7.092e+05', 'mean_token_accuracy': '0.992', 'epoch': '0.768'}   
{'loss': '0.01998', 'grad_norm': '0.1407', 'learning_rate': '1.409e-05', 'entropy': '0.02245', 'num_tokens': '7.239e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.784'}  
{'loss': '0.01945', 'grad_norm': '0.1622', 'learning_rate': '1.385e-05', 'entropy': '0.02239', 'num_tokens': '7.384e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.8'}    
{'loss': '0.01979', 'grad_norm': '0.1512', 'learning_rate': '1.361e-05', 'entropy': '0.02116', 'num_tokens': '7.535e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.816'}  
{'loss': '0.01768', 'grad_norm': '0.2099', 'learning_rate': '1.336e-05', 'entropy': '0.02079', 'num_tokens': '7.69e+05', 'mean_token_accuracy': '0.9943', 'epoch': '0.832'}   
{'loss': '0.01762', 'grad_norm': '0.1474', 'learning_rate': '1.312e-05', 'entropy': '0.02025', 'num_tokens': '7.84e+05', 'mean_token_accuracy': '0.994', 'epoch': '0.848'}    
{'loss': '0.02038', 'grad_norm': '0.2052', 'learning_rate': '1.287e-05', 'entropy': '0.02111', 'num_tokens': '7.988e+05', 'mean_token_accuracy': '0.9937', 'epoch': '0.864'}  
{'loss': '0.01938', 'grad_norm': '0.1649', 'learning_rate': '1.261e-05', 'entropy': '0.02144', 'num_tokens': '8.135e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.88'}   
{'loss': '0.02075', 'grad_norm': '0.2096', 'learning_rate': '1.236e-05', 'entropy': '0.02177', 'num_tokens': '8.283e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.896'}  
{'loss': '0.02067', 'grad_norm': '0.1516', 'learning_rate': '1.21e-05', 'entropy': '0.02333', 'num_tokens': '8.428e+05', 'mean_token_accuracy': '0.9924', 'epoch': '0.912'}   
{'loss': '0.0198', 'grad_norm': '0.2426', 'learning_rate': '1.185e-05', 'entropy': '0.02133', 'num_tokens': '8.574e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.928'}   
{'loss': '0.01951', 'grad_norm': '0.123', 'learning_rate': '1.159e-05', 'entropy': '0.02168', 'num_tokens': '8.722e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.944'}   
{'loss': '0.01865', 'grad_norm': '0.1615', 'learning_rate': '1.133e-05', 'entropy': '0.02076', 'num_tokens': '8.87e+05', 'mean_token_accuracy': '0.9938', 'epoch': '0.96'}    
{'loss': '0.0191', 'grad_norm': '0.1531', 'learning_rate': '1.107e-05', 'entropy': '0.02112', 'num_tokens': '9.017e+05', 'mean_token_accuracy': '0.9934', 'epoch': '0.976'}   
{'loss': '0.01861', 'grad_norm': '0.2012', 'learning_rate': '1.081e-05', 'entropy': '0.01968', 'num_tokens': '9.171e+05', 'mean_token_accuracy': '0.994', 'epoch': '0.992'}   
{'loss': '0.02001', 'grad_norm': '0.1668', 'learning_rate': '1.055e-05', 'entropy': '0.02192', 'num_tokens': '9.322e+05', 'mean_token_accuracy': '0.9931', 'epoch': '1.008'}  
{'loss': '0.0192', 'grad_norm': '0.1456', 'learning_rate': '1.029e-05', 'entropy': '0.02139', 'num_tokens': '9.472e+05', 'mean_token_accuracy': '0.9937', 'epoch': '1.024'}   
{'loss': '0.01963', 'grad_norm': '0.2527', 'learning_rate': '1.003e-05', 'entropy': '0.02196', 'num_tokens': '9.62e+05', 'mean_token_accuracy': '0.9932', 'epoch': '1.04'}    
{'loss': '0.01824', 'grad_norm': '0.1498', 'learning_rate': '9.764e-06', 'entropy': '0.02067', 'num_tokens': '9.767e+05', 'mean_token_accuracy': '0.9941', 'epoch': '1.056'}  
{'loss': '0.0214', 'grad_norm': '0.1704', 'learning_rate': '9.503e-06', 'entropy': '0.0224', 'num_tokens': '9.911e+05', 'mean_token_accuracy': '0.9924', 'epoch': '1.072'}    
{'loss': '0.01908', 'grad_norm': '0.1686', 'learning_rate': '9.242e-06', 'entropy': '0.0208', 'num_tokens': '1.006e+06', 'mean_token_accuracy': '0.9938', 'epoch': '1.088'}   
{'loss': '0.0186', 'grad_norm': '0.1204', 'learning_rate': '8.981e-06', 'entropy': '0.02158', 'num_tokens': '1.021e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.104'}   
{'loss': '0.01925', 'grad_norm': '0.15', 'learning_rate': '8.721e-06', 'entropy': '0.02141', 'num_tokens': '1.036e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.12'}     
{'loss': '0.01937', 'grad_norm': '0.1297', 'learning_rate': '8.462e-06', 'entropy': '0.02161', 'num_tokens': '1.051e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.136'}  
{'loss': '0.01984', 'grad_norm': '0.1198', 'learning_rate': '8.203e-06', 'entropy': '0.0226', 'num_tokens': '1.066e+06', 'mean_token_accuracy': '0.993', 'epoch': '1.152'}    
{'loss': '0.01849', 'grad_norm': '0.1897', 'learning_rate': '7.946e-06', 'entropy': '0.02131', 'num_tokens': '1.081e+06', 'mean_token_accuracy': '0.9939', 'epoch': '1.168'}  
{'loss': '0.02079', 'grad_norm': '0.1327', 'learning_rate': '7.691e-06', 'entropy': '0.02324', 'num_tokens': '1.095e+06', 'mean_token_accuracy': '0.9928', 'epoch': '1.184'}  
{'loss': '0.01882', 'grad_norm': '0.1433', 'learning_rate': '7.437e-06', 'entropy': '0.02059', 'num_tokens': '1.11e+06', 'mean_token_accuracy': '0.9936', 'epoch': '1.2'}     
{'loss': '0.01966', 'grad_norm': '0.1844', 'learning_rate': '7.185e-06', 'entropy': '0.02156', 'num_tokens': '1.125e+06', 'mean_token_accuracy': '0.9929', 'epoch': '1.216'}  
{'loss': '0.01871', 'grad_norm': '0.1775', 'learning_rate': '6.935e-06', 'entropy': '0.0211', 'num_tokens': '1.14e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.232'}    
{'loss': '0.01877', 'grad_norm': '0.1586', 'learning_rate': '6.687e-06', 'entropy': '0.02031', 'num_tokens': '1.154e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.248'}  
{'loss': '0.01786', 'grad_norm': '0.1603', 'learning_rate': '6.441e-06', 'entropy': '0.02028', 'num_tokens': '1.17e+06', 'mean_token_accuracy': '0.9939', 'epoch': '1.264'}   
{'loss': '0.01972', 'grad_norm': '0.1582', 'learning_rate': '6.197e-06', 'entropy': '0.02105', 'num_tokens': '1.185e+06', 'mean_token_accuracy': '0.9927', 'epoch': '1.28'}   
{'loss': '0.0203', 'grad_norm': '0.1967', 'learning_rate': '5.957e-06', 'entropy': '0.02133', 'num_tokens': '1.199e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.296'}   
{'loss': '0.01931', 'grad_norm': '0.1591', 'learning_rate': '5.719e-06', 'entropy': '0.02139', 'num_tokens': '1.213e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.312'}  
{'loss': '0.01904', 'grad_norm': '0.2433', 'learning_rate': '5.483e-06', 'entropy': '0.02124', 'num_tokens': '1.228e+06', 'mean_token_accuracy': '0.993', 'epoch': '1.328'}   
{'loss': '0.3829', 'grad_norm': '0.2547', 'learning_rate': '1.992e-05', 'entropy': '0.3698', 'num_tokens': '1.485e+05', 'mean_token_accuracy': '0.9033', 'epoch': '0.16'}     
{'loss': '0.3293', 'grad_norm': '0.3942', 'learning_rate': '1.988e-05', 'entropy': '0.3259', 'num_tokens': '1.634e+05', 'mean_token_accuracy': '0.9116', 'epoch': '0.176'}    
{'loss': '0.2721', 'grad_norm': '0.4019', 'learning_rate': '1.984e-05', 'entropy': '0.2561', 'num_tokens': '1.779e+05', 'mean_token_accuracy': '0.9275', 'epoch': '0.192'}    
{'loss': '0.2275', 'grad_norm': '0.8416', 'learning_rate': '1.979e-05', 'entropy': '0.2302', 'num_tokens': '1.925e+05', 'mean_token_accuracy': '0.9366', 'epoch': '0.208'}    
{'loss': '0.1888', 'grad_norm': '0.5342', 'learning_rate': '1.973e-05', 'entropy': '0.2052', 'num_tokens': '2.074e+05', 'mean_token_accuracy': '0.9462', 'epoch': '0.224'}    
{'loss': '0.1398', 'grad_norm': '0.6558', 'learning_rate': '1.967e-05', 'entropy': '0.1614', 'num_tokens': '2.222e+05', 'mean_token_accuracy': '0.9603', 'epoch': '0.24'}     
{'loss': '0.1252', 'grad_norm': '1.051', 'learning_rate': '1.96e-05', 'entropy': '0.147', 'num_tokens': '2.372e+05', 'mean_token_accuracy': '0.9643', 'epoch': '0.256'}       
{'loss': '0.08375', 'grad_norm': '0.6069', 'learning_rate': '1.952e-05', 'entropy': '0.1121', 'num_tokens': '2.518e+05', 'mean_token_accuracy': '0.9786', 'epoch': '0.272'}   
{'loss': '0.05325', 'grad_norm': '1.373', 'learning_rate': '1.944e-05', 'entropy': '0.08118', 'num_tokens': '2.67e+05', 'mean_token_accuracy': '0.9872', 'epoch': '0.288'}    
{'loss': '0.04104', 'grad_norm': '0.6528', 'learning_rate': '1.935e-05', 'entropy': '0.06192', 'num_tokens': '2.817e+05', 'mean_token_accuracy': '0.9899', 'epoch': '0.304'}  
{'loss': '0.02892', 'grad_norm': '0.4461', 'learning_rate': '1.925e-05', 'entropy': '0.04384', 'num_tokens': '2.961e+05', 'mean_token_accuracy': '0.9922', 'epoch': '0.32'}   
{'loss': '0.02947', 'grad_norm': '0.3217', 'learning_rate': '1.915e-05', 'entropy': '0.04165', 'num_tokens': '3.101e+05', 'mean_token_accuracy': '0.9921', 'epoch': '0.336'}  
{'loss': '0.02626', 'grad_norm': '0.3799', 'learning_rate': '1.904e-05', 'entropy': '0.03441', 'num_tokens': '3.251e+05', 'mean_token_accuracy': '0.9929', 'epoch': '0.352'}  
{'loss': '0.02591', 'grad_norm': '0.6662', 'learning_rate': '1.892e-05', 'entropy': '0.0356', 'num_tokens': '3.394e+05', 'mean_token_accuracy': '0.9927', 'epoch': '0.368'}   
{'loss': '0.02339', 'grad_norm': '0.4929', 'learning_rate': '1.88e-05', 'entropy': '0.02855', 'num_tokens': '3.543e+05', 'mean_token_accuracy': '0.9934', 'epoch': '0.384'}   
{'loss': '0.02305', 'grad_norm': '0.1569', 'learning_rate': '1.867e-05', 'entropy': '0.03111', 'num_tokens': '3.688e+05', 'mean_token_accuracy': '0.9934', 'epoch': '0.4'}    
{'loss': '0.02159', 'grad_norm': '0.2829', 'learning_rate': '1.854e-05', 'entropy': '0.02673', 'num_tokens': '3.838e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.416'}  
{'loss': '0.02293', 'grad_norm': '0.2877', 'learning_rate': '1.84e-05', 'entropy': '0.02935', 'num_tokens': '3.988e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.432'}    
{'loss': '0.02206', 'grad_norm': '0.4176', 'learning_rate': '1.826e-05', 'entropy': '0.02624', 'num_tokens': '4.134e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.448'}  
{'loss': '0.02168', 'grad_norm': '0.2395', 'learning_rate': '1.811e-05', 'entropy': '0.02608', 'num_tokens': '4.288e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.464'}   
{'loss': '0.02129', 'grad_norm': '0.2514', 'learning_rate': '1.795e-05', 'entropy': '0.02709', 'num_tokens': '4.44e+05', 'mean_token_accuracy': '0.9933', 'epoch': '0.48'}    
{'loss': '0.02007', 'grad_norm': '0.258', 'learning_rate': '1.779e-05', 'entropy': '0.02295', 'num_tokens': '4.587e+05', 'mean_token_accuracy': '0.994', 'epoch': '0.496'}    
{'loss': '0.02287', 'grad_norm': '0.3909', 'learning_rate': '1.762e-05', 'entropy': '0.02635', 'num_tokens': '4.732e+05', 'mean_token_accuracy': '0.9929', 'epoch': '0.512'}  
{'loss': '0.02058', 'grad_norm': '0.1566', 'learning_rate': '1.745e-05', 'entropy': '0.02542', 'num_tokens': '4.885e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.528'}   
{'loss': '0.02057', 'grad_norm': '0.1831', 'learning_rate': '1.727e-05', 'entropy': '0.02517', 'num_tokens': '5.032e+05', 'mean_token_accuracy': '0.9928', 'epoch': '0.544'}  
{'loss': '0.01957', 'grad_norm': '0.2452', 'learning_rate': '1.709e-05', 'entropy': '0.02287', 'num_tokens': '5.182e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.56'}   
{'loss': '0.02065', 'grad_norm': '0.1433', 'learning_rate': '1.69e-05', 'entropy': '0.02422', 'num_tokens': '5.329e+05', 'mean_token_accuracy': '0.9933', 'epoch': '0.576'}   
{'loss': '0.02171', 'grad_norm': '0.2663', 'learning_rate': '1.671e-05', 'entropy': '0.02456', 'num_tokens': '5.474e+05', 'mean_token_accuracy': '0.9925', 'epoch': '0.592'}  
{'loss': '0.02047', 'grad_norm': '0.3068', 'learning_rate': '1.651e-05', 'entropy': '0.02158', 'num_tokens': '5.626e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.608'}  
{'loss': '0.02159', 'grad_norm': '0.2054', 'learning_rate': '1.631e-05', 'entropy': '0.02582', 'num_tokens': '5.769e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.624'}   
{'loss': '0.02042', 'grad_norm': '0.2311', 'learning_rate': '1.611e-05', 'entropy': '0.02434', 'num_tokens': '5.916e+05', 'mean_token_accuracy': '0.993', 'epoch': '0.64'}    
{'loss': '0.02107', 'grad_norm': '0.2707', 'learning_rate': '1.59e-05', 'entropy': '0.02322', 'num_tokens': '6.062e+05', 'mean_token_accuracy': '0.9932', 'epoch': '0.656'}   
{'loss': '0.01989', 'grad_norm': '0.2326', 'learning_rate': '1.569e-05', 'entropy': '0.02246', 'num_tokens': '6.208e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.672'}  
{'loss': '0.01919', 'grad_norm': '0.2651', 'learning_rate': '1.547e-05', 'entropy': '0.02121', 'num_tokens': '6.364e+05', 'mean_token_accuracy': '0.9932', 'epoch': '0.688'}  
{'loss': '0.02145', 'grad_norm': '0.1585', 'learning_rate': '1.525e-05', 'entropy': '0.02321', 'num_tokens': '6.503e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.704'}  
{'loss': '0.01823', 'grad_norm': '0.1366', 'learning_rate': '1.502e-05', 'entropy': '0.02258', 'num_tokens': '6.655e+05', 'mean_token_accuracy': '0.9941', 'epoch': '0.72'}   
{'loss': '0.02124', 'grad_norm': '0.1948', 'learning_rate': '1.479e-05', 'entropy': '0.02333', 'num_tokens': '6.801e+05', 'mean_token_accuracy': '0.9929', 'epoch': '0.736'}  
{'loss': '0.01946', 'grad_norm': '0.1781', 'learning_rate': '1.456e-05', 'entropy': '0.02164', 'num_tokens': '6.946e+05', 'mean_token_accuracy': '0.9939', 'epoch': '0.752'}  
{'loss': '0.02157', 'grad_norm': '0.2754', 'learning_rate': '1.433e-05', 'entropy': '0.02332', 'num_tokens': '7.092e+05', 'mean_token_accuracy': '0.992', 'epoch': '0.768'}   
{'loss': '0.01998', 'grad_norm': '0.1407', 'learning_rate': '1.409e-05', 'entropy': '0.02245', 'num_tokens': '7.239e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.784'}  
{'loss': '0.01945', 'grad_norm': '0.1622', 'learning_rate': '1.385e-05', 'entropy': '0.02239', 'num_tokens': '7.384e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.8'}    
{'loss': '0.01979', 'grad_norm': '0.1512', 'learning_rate': '1.361e-05', 'entropy': '0.02116', 'num_tokens': '7.535e+05', 'mean_token_accuracy': '0.9935', 'epoch': '0.816'}  
{'loss': '0.01768', 'grad_norm': '0.2099', 'learning_rate': '1.336e-05', 'entropy': '0.02079', 'num_tokens': '7.69e+05', 'mean_token_accuracy': '0.9943', 'epoch': '0.832'}   
{'loss': '0.01762', 'grad_norm': '0.1474', 'learning_rate': '1.312e-05', 'entropy': '0.02025', 'num_tokens': '7.84e+05', 'mean_token_accuracy': '0.994', 'epoch': '0.848'}    
{'loss': '0.02038', 'grad_norm': '0.2052', 'learning_rate': '1.287e-05', 'entropy': '0.02111', 'num_tokens': '7.988e+05', 'mean_token_accuracy': '0.9937', 'epoch': '0.864'}  
{'loss': '0.01938', 'grad_norm': '0.1649', 'learning_rate': '1.261e-05', 'entropy': '0.02144', 'num_tokens': '8.135e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.88'}   
{'loss': '0.02075', 'grad_norm': '0.2096', 'learning_rate': '1.236e-05', 'entropy': '0.02177', 'num_tokens': '8.283e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.896'}  
{'loss': '0.02067', 'grad_norm': '0.1516', 'learning_rate': '1.21e-05', 'entropy': '0.02333', 'num_tokens': '8.428e+05', 'mean_token_accuracy': '0.9924', 'epoch': '0.912'}   
{'loss': '0.0198', 'grad_norm': '0.2426', 'learning_rate': '1.185e-05', 'entropy': '0.02133', 'num_tokens': '8.574e+05', 'mean_token_accuracy': '0.9931', 'epoch': '0.928'}   
{'loss': '0.01951', 'grad_norm': '0.123', 'learning_rate': '1.159e-05', 'entropy': '0.02168', 'num_tokens': '8.722e+05', 'mean_token_accuracy': '0.9936', 'epoch': '0.944'}   
{'loss': '0.01865', 'grad_norm': '0.1615', 'learning_rate': '1.133e-05', 'entropy': '0.02076', 'num_tokens': '8.87e+05', 'mean_token_accuracy': '0.9938', 'epoch': '0.96'}    
{'loss': '0.0191', 'grad_norm': '0.1531', 'learning_rate': '1.107e-05', 'entropy': '0.02112', 'num_tokens': '9.017e+05', 'mean_token_accuracy': '0.9934', 'epoch': '0.976'}   
{'loss': '0.01861', 'grad_norm': '0.2012', 'learning_rate': '1.081e-05', 'entropy': '0.01968', 'num_tokens': '9.171e+05', 'mean_token_accuracy': '0.994', 'epoch': '0.992'}   
{'loss': '0.02001', 'grad_norm': '0.1668', 'learning_rate': '1.055e-05', 'entropy': '0.02192', 'num_tokens': '9.322e+05', 'mean_token_accuracy': '0.9931', 'epoch': '1.008'}  
{'loss': '0.0192', 'grad_norm': '0.1456', 'learning_rate': '1.029e-05', 'entropy': '0.02139', 'num_tokens': '9.472e+05', 'mean_token_accuracy': '0.9937', 'epoch': '1.024'}   
{'loss': '0.01963', 'grad_norm': '0.2527', 'learning_rate': '1.003e-05', 'entropy': '0.02196', 'num_tokens': '9.62e+05', 'mean_token_accuracy': '0.9932', 'epoch': '1.04'}    
{'loss': '0.01824', 'grad_norm': '0.1498', 'learning_rate': '9.764e-06', 'entropy': '0.02067', 'num_tokens': '9.767e+05', 'mean_token_accuracy': '0.9941', 'epoch': '1.056'}  
{'loss': '0.0214', 'grad_norm': '0.1704', 'learning_rate': '9.503e-06', 'entropy': '0.0224', 'num_tokens': '9.911e+05', 'mean_token_accuracy': '0.9924', 'epoch': '1.072'}    
{'loss': '0.01908', 'grad_norm': '0.1686', 'learning_rate': '9.242e-06', 'entropy': '0.0208', 'num_tokens': '1.006e+06', 'mean_token_accuracy': '0.9938', 'epoch': '1.088'}   
{'loss': '0.0186', 'grad_norm': '0.1204', 'learning_rate': '8.981e-06', 'entropy': '0.02158', 'num_tokens': '1.021e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.104'}   
{'loss': '0.01925', 'grad_norm': '0.15', 'learning_rate': '8.721e-06', 'entropy': '0.02141', 'num_tokens': '1.036e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.12'}     
{'loss': '0.01937', 'grad_norm': '0.1297', 'learning_rate': '8.462e-06', 'entropy': '0.02161', 'num_tokens': '1.051e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.136'}  
{'loss': '0.01984', 'grad_norm': '0.1198', 'learning_rate': '8.203e-06', 'entropy': '0.0226', 'num_tokens': '1.066e+06', 'mean_token_accuracy': '0.993', 'epoch': '1.152'}    
{'loss': '0.01849', 'grad_norm': '0.1897', 'learning_rate': '7.946e-06', 'entropy': '0.02131', 'num_tokens': '1.081e+06', 'mean_token_accuracy': '0.9939', 'epoch': '1.168'}  
{'loss': '0.02079', 'grad_norm': '0.1327', 'learning_rate': '7.691e-06', 'entropy': '0.02324', 'num_tokens': '1.095e+06', 'mean_token_accuracy': '0.9928', 'epoch': '1.184'}  
{'loss': '0.01882', 'grad_norm': '0.1433', 'learning_rate': '7.437e-06', 'entropy': '0.02059', 'num_tokens': '1.11e+06', 'mean_token_accuracy': '0.9936', 'epoch': '1.2'}     
{'loss': '0.01966', 'grad_norm': '0.1844', 'learning_rate': '7.185e-06', 'entropy': '0.02156', 'num_tokens': '1.125e+06', 'mean_token_accuracy': '0.9929', 'epoch': '1.216'}  
{'loss': '0.01871', 'grad_norm': '0.1775', 'learning_rate': '6.935e-06', 'entropy': '0.0211', 'num_tokens': '1.14e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.232'}    
{'loss': '0.01877', 'grad_norm': '0.1586', 'learning_rate': '6.687e-06', 'entropy': '0.02031', 'num_tokens': '1.154e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.248'}  
{'loss': '0.01786', 'grad_norm': '0.1603', 'learning_rate': '6.441e-06', 'entropy': '0.02028', 'num_tokens': '1.17e+06', 'mean_token_accuracy': '0.9939', 'epoch': '1.264'}   
{'loss': '0.01972', 'grad_norm': '0.1582', 'learning_rate': '6.197e-06', 'entropy': '0.02105', 'num_tokens': '1.185e+06', 'mean_token_accuracy': '0.9927', 'epoch': '1.28'}   
{'loss': '0.0203', 'grad_norm': '0.1967', 'learning_rate': '5.957e-06', 'entropy': '0.02133', 'num_tokens': '1.199e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.296'}   
{'loss': '0.01931', 'grad_norm': '0.1591', 'learning_rate': '5.719e-06', 'entropy': '0.02139', 'num_tokens': '1.213e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.312'}  
{'loss': '0.01904', 'grad_norm': '0.2433', 'learning_rate': '5.483e-06', 'entropy': '0.02124', 'num_tokens': '1.228e+06', 'mean_token_accuracy': '0.993', 'epoch': '1.328'}   
{'loss': '0.01902', 'grad_norm': '0.1317', 'learning_rate': '5.251e-06', 'entropy': '0.0205', 'num_tokens': '1.243e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.344'}   
{'loss': '0.01908', 'grad_norm': '0.136', 'learning_rate': '5.023e-06', 'entropy': '0.02074', 'num_tokens': '1.258e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.36'}    
{'loss': '0.01912', 'grad_norm': '0.1496', 'learning_rate': '4.797e-06', 'entropy': '0.02056', 'num_tokens': '1.272e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.376'}  
{'loss': '0.01985', 'grad_norm': '0.1672', 'learning_rate': '4.576e-06', 'entropy': '0.02155', 'num_tokens': '1.287e+06', 'mean_token_accuracy': '0.9928', 'epoch': '1.392'}  
{'loss': '0.01923', 'grad_norm': '0.211', 'learning_rate': '4.358e-06', 'entropy': '0.02126', 'num_tokens': '1.301e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.408'}   
{'loss': '0.01947', 'grad_norm': '0.289', 'learning_rate': '4.143e-06', 'entropy': '0.02145', 'num_tokens': '1.316e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.424'}   
{'loss': '0.01794', 'grad_norm': '0.1897', 'learning_rate': '3.933e-06', 'entropy': '0.02013', 'num_tokens': '1.331e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.44'}   
{'loss': '0.0201', 'grad_norm': '0.1547', 'learning_rate': '3.727e-06', 'entropy': '0.02126', 'num_tokens': '1.346e+06', 'mean_token_accuracy': '0.9926', 'epoch': '1.456'}   
{'loss': '0.01787', 'grad_norm': '0.1703', 'learning_rate': '3.525e-06', 'entropy': '0.02034', 'num_tokens': '1.361e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.472'}  
{'loss': '0.01949', 'grad_norm': '0.2152', 'learning_rate': '3.328e-06', 'entropy': '0.02127', 'num_tokens': '1.376e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.488'}  
{'loss': '0.01916', 'grad_norm': '0.1562', 'learning_rate': '3.135e-06', 'entropy': '0.02144', 'num_tokens': '1.391e+06', 'mean_token_accuracy': '0.993', 'epoch': '1.504'}   
{'loss': '0.01832', 'grad_norm': '0.1488', 'learning_rate': '2.947e-06', 'entropy': '0.02014', 'num_tokens': '1.406e+06', 'mean_token_accuracy': '0.9939', 'epoch': '1.52'}   
{'loss': '0.0192', 'grad_norm': '0.1469', 'learning_rate': '2.764e-06', 'entropy': '0.02089', 'num_tokens': '1.42e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.536'}    
{'loss': '0.01853', 'grad_norm': '0.1558', 'learning_rate': '2.586e-06', 'entropy': '0.02074', 'num_tokens': '1.435e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.552'}  
{'loss': '0.01958', 'grad_norm': '0.1694', 'learning_rate': '2.413e-06', 'entropy': '0.02138', 'num_tokens': '1.449e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.568'}  
{'loss': '0.01915', 'grad_norm': '0.158', 'learning_rate': '2.245e-06', 'entropy': '0.02076', 'num_tokens': '1.464e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.584'}   
{'loss': '0.01898', 'grad_norm': '0.184', 'learning_rate': '2.082e-06', 'entropy': '0.02078', 'num_tokens': '1.479e+06', 'mean_token_accuracy': '0.9932', 'epoch': '1.6'}     
{'loss': '0.01914', 'grad_norm': '0.183', 'learning_rate': '1.925e-06', 'entropy': '0.02137', 'num_tokens': '1.494e+06', 'mean_token_accuracy': '0.9928', 'epoch': '1.616'}   
{'loss': '0.01821', 'grad_norm': '0.16', 'learning_rate': '1.774e-06', 'entropy': '0.02032', 'num_tokens': '1.509e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.632'}    
{'loss': '0.01858', 'grad_norm': '0.157', 'learning_rate': '1.628e-06', 'entropy': '0.02056', 'num_tokens': '1.524e+06', 'mean_token_accuracy': '0.9932', 'epoch': '1.648'}   
{'loss': '0.01907', 'grad_norm': '0.2083', 'learning_rate': '1.487e-06', 'entropy': '0.02086', 'num_tokens': '1.539e+06', 'mean_token_accuracy': '0.9933', 'epoch': '1.664'}  
{'loss': '0.01892', 'grad_norm': '0.1921', 'learning_rate': '1.353e-06', 'entropy': '0.02044', 'num_tokens': '1.553e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.68'}   
{'loss': '0.01783', 'grad_norm': '0.1277', 'learning_rate': '1.224e-06', 'entropy': '0.01979', 'num_tokens': '1.568e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.696'}  
{'loss': '0.01861', 'grad_norm': '0.1563', 'learning_rate': '1.102e-06', 'entropy': '0.02043', 'num_tokens': '1.583e+06', 'mean_token_accuracy': '0.9936', 'epoch': '1.712'}  
{'loss': '0.01914', 'grad_norm': '0.199', 'learning_rate': '9.854e-07', 'entropy': '0.02143', 'num_tokens': '1.597e+06', 'mean_token_accuracy': '0.9932', 'epoch': '1.728'}   
{'loss': '0.01897', 'grad_norm': '0.1623', 'learning_rate': '8.752e-07', 'entropy': '0.02039', 'num_tokens': '1.612e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.744'}  
{'loss': '0.0176', 'grad_norm': '0.2016', 'learning_rate': '7.713e-07', 'entropy': '0.01969', 'num_tokens': '1.627e+06', 'mean_token_accuracy': '0.9936', 'epoch': '1.76'}
{'loss': '0.01854', 'grad_norm': '0.241', 'learning_rate': '6.736e-07', 'entropy': '0.02074', 'num_tokens': '1.642e+06', 'mean_token_accuracy': '0.9936', 'epoch': '1.776'}
{'loss': '0.01852', 'grad_norm': '0.1511', 'learning_rate': '5.824e-07', 'entropy': '0.02049', 'num_tokens': '1.657e+06', 'mean_token_accuracy': '0.9936', 'epoch': '1.792'}
{'loss': '0.01892', 'grad_norm': '0.2078', 'learning_rate': '4.976e-07', 'entropy': '0.02116', 'num_tokens': '1.671e+06', 'mean_token_accuracy': '0.9935', 'epoch': '1.808'}
{'loss': '0.01871', 'grad_norm': '0.1461', 'learning_rate': '4.193e-07', 'entropy': '0.02094', 'num_tokens': '1.686e+06', 'mean_token_accuracy': '0.9934', 'epoch': '1.824'}
{'loss': '0.01828', 'grad_norm': '0.1926', 'learning_rate': '3.476e-07', 'entropy': '0.02029', 'num_tokens': '1.701e+06', 'mean_token_accuracy': '0.9937', 'epoch': '1.84'}
{'loss': '0.01683', 'grad_norm': '0.1836', 'learning_rate': '2.824e-07', 'entropy': '0.01909', 'num_tokens': '1.717e+06', 'mean_token_accuracy': '0.994', 'epoch': '1.856'}
{'loss': '0.01804', 'grad_norm': '0.1466', 'learning_rate': '2.24e-07', 'entropy': '0.02042', 'num_tokens': '1.731e+06', 'mean_token_accuracy': '0.994', 'epoch': '1.872'}
{'loss': '0.01734', 'grad_norm': '0.1507', 'learning_rate': '1.723e-07', 'entropy': '0.0195', 'num_tokens': '1.746e+06', 'mean_token_accuracy': '0.9941', 'epoch': '1.888'}
{'loss': '0.01964', 'grad_norm': '0.1359', 'learning_rate': '1.272e-07', 'entropy': '0.02156', 'num_tokens': '1.761e+06', 'mean_token_accuracy': '0.9927', 'epoch': '1.904'}
{'loss': '0.01793', 'grad_norm': '0.1884', 'learning_rate': '8.9e-08', 'entropy': '0.01957', 'num_tokens': '1.776e+06', 'mean_token_accuracy': '0.994', 'epoch': '1.92'}
{'loss': '0.01902', 'grad_norm': '0.1808', 'learning_rate': '5.755e-08', 'entropy': '0.02087', 'num_tokens': '1.79e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.936'}
{'loss': '0.01922', 'grad_norm': '0.1695', 'learning_rate': '3.291e-08', 'entropy': '0.02157', 'num_tokens': '1.804e+06', 'mean_token_accuracy': '0.993', 'epoch': '1.952'}
{'loss': '0.01852', 'grad_norm': '0.118', 'learning_rate': '1.511e-08', 'entropy': '0.02044', 'num_tokens': '1.819e+06', 'mean_token_accuracy': '0.9931', 'epoch': '1.968'}
{'loss': '0.01902', 'grad_norm': '0.147', 'learning_rate': '4.146e-09', 'entropy': '0.02112', 'num_tokens': '1.834e+06', 'mean_token_accuracy': '0.9938', 'epoch': '1.984'}
{'loss': '0.01949', 'grad_norm': '0.1702', 'learning_rate': '3.427e-11', 'entropy': '0.02122', 'num_tokens': '1.849e+06', 'mean_token_accuracy': '0.9929', 'epoch': '2'}
{'train_runtime': '3520', 'train_samples_per_second': '2.841', 'train_steps_per_second': '0.355', 'train_loss': '0.1152', 'epoch': '2'} 
100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1250/1250 [58:40<00:00,  2.82s/it]
✅ Training Complete! Weights saved to: avca-remediation-lora-bf16/final_adapter