python ../../learn/training.py ../../mimicdata/mimic3/train_full.csv ../../mimicdata/mimic3/vocab.csv full conv_attn 200 --filter-size 10 --num-filter-maps 50 --dropout 0.2 --patience 10 --lr 0.0001 --criterion prec_at_8 --embed-file ../../mimicdata/mimic3/processed_full.embed --gpu
#500个卷积核
python ../../learn/training.py ../../mimicdata/mimic3/train_full.csv ../../mimicdata/mimic3/vocab.csv full conv_attn 40 --filter-size 10 --num-filter-maps 500 --dropout 0.2 --patience 10 --lr 0.0001 --criterion prec_at_8 --embed-file ../../mimicdata/mimic3/processed_full.embed --gpu
