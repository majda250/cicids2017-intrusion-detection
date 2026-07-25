from pydantic import BaseModel, Field, ConfigDict


class PredictionInput(BaseModel):

    model_config = ConfigDict(
        populate_by_name=True
    )

    destination_port: float = Field(..., alias=" Destination Port")
    flow_duration: float = Field(..., alias=" Flow Duration")
    total_fwd_packets: float = Field(..., alias=" Total Fwd Packets")
    total_backward_packets: float = Field(..., alias=" Total Backward Packets")
    total_length_fwd_packets: float = Field(..., alias="Total Length of Fwd Packets")
    fwd_packet_length_min: float = Field(..., alias=" Fwd Packet Length Min")
    fwd_packet_length_mean: float = Field(..., alias=" Fwd Packet Length Mean")
    fwd_packet_length_std: float = Field(..., alias=" Fwd Packet Length Std")
    bwd_packet_length_min: float = Field(..., alias=" Bwd Packet Length Min")
    bwd_packet_length_mean: float = Field(..., alias=" Bwd Packet Length Mean")
    flow_bytes_s: float = Field(..., alias="Flow Bytes/s")
    flow_iat_std: float = Field(..., alias=" Flow IAT Std")
    flow_iat_min: float = Field(..., alias=" Flow IAT Min")
    fwd_iat_mean: float = Field(..., alias=" Fwd IAT Mean")
    fwd_iat_std: float = Field(..., alias=" Fwd IAT Std")
    fwd_iat_min: float = Field(..., alias=" Fwd IAT Min")
    bwd_iat_total: float = Field(..., alias="Bwd IAT Total")
    bwd_iat_std: float = Field(..., alias=" Bwd IAT Std")
    bwd_iat_max: float = Field(..., alias=" Bwd IAT Max")
    bwd_iat_min: float = Field(..., alias=" Bwd IAT Min")
    fwd_psh_flags: float = Field(..., alias="Fwd PSH Flags")
    fwd_urg_flags: float = Field(..., alias=" Fwd URG Flags")
    fwd_header_length: float = Field(..., alias=" Fwd Header Length")
    bwd_header_length: float = Field(..., alias=" Bwd Header Length")
    fwd_packets_s: float = Field(..., alias="Fwd Packets/s")
    bwd_packets_s: float = Field(..., alias=" Bwd Packets/s")
    min_packet_length: float = Field(..., alias=" Min Packet Length")
    packet_length_variance: float = Field(..., alias=" Packet Length Variance")
    fin_flag_count: float = Field(..., alias="FIN Flag Count")
    syn_flag_count: float = Field(..., alias=" SYN Flag Count")
    rst_flag_count: float = Field(..., alias=" RST Flag Count")
    psh_flag_count: float = Field(..., alias=" PSH Flag Count")
    ack_flag_count: float = Field(..., alias=" ACK Flag Count")
    urg_flag_count: float = Field(..., alias=" URG Flag Count")
    cwe_flag_count: float = Field(..., alias=" CWE Flag Count")
    down_up_ratio: float = Field(..., alias=" Down/Up Ratio")
    avg_fwd_segment_size: float = Field(..., alias=" Avg Fwd Segment Size")
    fwd_header_length_1: float = Field(..., alias=" Fwd Header Length.1")
    subflow_bwd_packets: float = Field(..., alias=" Subflow Bwd Packets")
    init_win_bytes_forward: float = Field(..., alias="Init_Win_bytes_forward")
    init_win_bytes_backward: float = Field(..., alias=" Init_Win_bytes_backward")
    act_data_pkt_fwd: float = Field(..., alias=" act_data_pkt_fwd")
    min_seg_size_forward: float = Field(..., alias=" min_seg_size_forward")
    active_mean: float = Field(..., alias="Active Mean")
    active_std: float = Field(..., alias=" Active Std")
    active_max: float = Field(..., alias=" Active Max")
    idle_std: float = Field(..., alias=" Idle Std")


class PredictionOutput(BaseModel):
    prediction: int
    label: str