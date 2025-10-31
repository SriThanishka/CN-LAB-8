from dataclasses import dataclass

# 1. Packet Class

@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int  # 0 = High, 1 = Medium, 2 = Low

# 2. FIFO Scheduler
def fifo_scheduler(packet_list: list) -> list:
    """
    Simulate a FIFO (First-In-First-Out) scheduler.
    Returns packets in the same order they arrived.
    """
    # In FIFO, packets are sent in the exact order of arrival
    return packet_list.copy()


# 3. Priority Scheduler
def priority_scheduler(packet_list: list) -> list:
    """
    Simulate a Priority Scheduler.
    Packets with lower priority number (higher priority) are sent first.
    """
    # Sort by priority (0 first, then 1, then 2)
    # sorted() is stable in Python, so arrival order is preserved
    return sorted(packet_list, key=lambda p: p.priority)


# 4. Test Case (Run this file directly to test)
if __name__ == "__main__":
    packets = [
        Packet("10.0.0.1", "10.0.0.2", "Data Packet 1", 2),
        Packet("10.0.0.1", "10.0.0.2", "Data Packet 2", 2),
        Packet("10.0.0.3", "10.0.0.4", "VOIP Packet 1", 0),
        Packet("10.0.0.5", "10.0.0.6", "Video Packet 1", 1),
        Packet("10.0.0.7", "10.0.0.8", "VOIP Packet 2", 0)
    ]

    # FIFO Scheduling Test
    fifo_result = fifo_scheduler(packets)
    print("FIFO Scheduler Output:")
    print([p.payload for p in fifo_result])

    # Priority Scheduling Test
    priority_result = priority_scheduler(packets)
    print("\nPriority Scheduler Output:")
    print([p.payload for p in priority_result])